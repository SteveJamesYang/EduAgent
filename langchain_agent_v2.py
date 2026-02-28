import os
import json
import requests
import re
import unicodedata
from bs4 import BeautifulSoup
from readability import Document

from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.agents import AgentAction, AgentFinish
from langchain_community.utilities import SearchApiAPIWrapper
from langchain_core.tools import tool
from openai import OpenAI
from typing import List, Tuple, Any, Dict

_SURROGATE_RE = re.compile(r'[\ud800-\udfff]')

# ========= 从 config/config.json 读取 API Key =========

def load_api_config() -> dict:
    """
    从 ./config/config.json 加载配置。
    如果文件不存在或解析失败，返回空 dict。
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cfg_path = os.path.join(base_dir, "config", "config.json")
    if not os.path.exists(cfg_path):
        print(f"[warn] 未找到配置文件: {cfg_path}，将仅使用已有环境变量中的 API Key")
        return {}
    try:
        with open(cfg_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print(f"[warn] 配置文件 {cfg_path} 内容不是 JSON 对象，将忽略。")
            return {}
        return data
    except Exception as e:
        print(f"[warn] 解析配置文件 {cfg_path} 失败: {e}，将仅使用环境变量中的 API Key")
        return {}

_API_CFG = load_api_config()


def ensure_env_key(name: str, required: bool = False) -> str | None:
    """
    确保某个 API Key 存在于环境变量中：
    - 优先使用已经存在的环境变量；
    - 否则从 _API_CFG 中读取并写入 os.environ；
    - 如果 required=True 且最终仍没有，抛出 RuntimeError。
    """
    val = os.getenv(name)
    if val:
        return val

    if name in _API_CFG and _API_CFG[name]:
        val = str(_API_CFG[name])
        os.environ[name] = val
        return val

    if required:
        raise RuntimeError(
            f"[fatal] 必需的 API Key '{name}' 未在环境变量或 config/config.json 中找到。"
        )
    else:
        print(f"[warn] 可选 API Key '{name}' 未设置，相关工具可能无法使用。")
        return None


# 说明：LLM 的 Key 会在 build_llm() 中按所选提供方按需检查；这里仅检查工具相关的可选 Key
ensure_env_key("SEARCHAPI_API_KEY", required=False)
# Tavily 的 Key 在真正构建 TavilySearch 工具时再按需 ensure_env_key("TAVILY_API_KEY")


def env_flag(name: str, default: bool = True) -> bool:
    """
    从环境变量读取一个布尔开关：
    - 未设置 => default
    - 允许的"真"值：1 / true / yes / y / on（不区分大小写）
    - 允许的"假"值：0 / false / no / n / off
    """
    v = os.getenv(name)
    if v is None:
        return default
    v = v.strip().lower()
    if v in ("1", "true", "yes", "y", "on"):
        return True
    if v in ("0", "false", "no", "n", "off"):
        return False
    return default


def fix_surrogates(s: str) -> str:
    """把潜在的 UTF-16 代理对"复原"为真实字符。"""
    if not isinstance(s, str):
        return s
    b = s.encode('utf-16', 'surrogatepass')
    s2 = b.decode('utf-16', 'ignore')  # ignore=丢弃孤立代理
    s2 = _SURROGATE_RE.sub('', s2)
    return unicodedata.normalize('NFC', s2)


def clean_text(obj):
    """递归清洗：修复代理 → 删除残留代理 → 保证可 UTF-8 编码。"""
    if isinstance(obj, str):
        s = fix_surrogates(obj)
        # 极端兜底：任何仍不可编码的字符都忽略
        return s.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
    elif isinstance(obj, dict):
        return {k: clean_text(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        t = [clean_text(x) for x in obj]
        return type(obj)(t) if not isinstance(obj, tuple) else tuple(t)
    return obj


# ========= LLM 本体（可通过命令行/环境变量切换） =========
# 约定：
#   - eval_computer_exam_alltypes.py 里可用 --llm deepseek/qwen/doubao/kimi/mimo（默认 deepseek）
#   - 也可直接设置环境变量：EDUAGENT_LLM=deepseek|qwen|doubao|kimi|mimo
#   - 可选覆盖：EDUAGENT_LLM_MODEL / EDUAGENT_LLM_BASE_URL
#   - Qwen 兼容 OpenAI Mode：base_url 默认 https://dashscope-intl.aliyuncs.com/compatible-mode/v1
#   - Doubao(方舟) 数据面 API：base_url 默认 https://ark.cn-beijing.volces.com/api/v3/
#   - Kimi：base_url 默认 https://api.moonshot.cn/v1
#   - Mimo（小米）：base_url 默认 https://api.mi.ai/v1
#
# 注意：Doubao 的 model 往往是你在控制台里看到的 "Model ID"，必须自行填写。

def ensure_any_env_key(names: list[str], required: bool = False, alias: str = "") -> str | None:
    """在多个候选环境变量名里寻找 API Key；也会尝试从 config/config.json 写入到环境变量。"""
    for n in names:
        v = os.getenv(n)
        if v:
            return v
    for n in names:
        if n in _API_CFG and _API_CFG[n]:
            v = str(_API_CFG[n])
            os.environ[n] = v
            return v
    if required:
        hint = alias or ("/".join(names))
        raise RuntimeError(f"[fatal] 必需的 API Key '{hint}' 未在环境变量或 config/config.json 中找到。")
    return None


def get_cfg_or_env(names: list[str], default: str = "") -> str:
    """按优先级读取配置值：环境变量 -> config/config.json -> default。"""
    for n in names:
        v = os.getenv(n)
        if v is not None and str(v).strip() != "":
            return str(v).strip()
    for n in names:
        if n in _API_CFG and str(_API_CFG[n]).strip() != "":
            return str(_API_CFG[n]).strip()
    return default


def build_llm():
    provider = (os.getenv("EDUAGENT_LLM", "deepseek") or "deepseek").strip().lower()
    # provider = (os.getenv("EDUAGENT_LLM", "mimo") or "mimo").strip().lower()
    # provider = (os.getenv("EDUAGENT_LLM", "kimi") or "kimi").strip().lower()
    # provider = (os.getenv("EDUAGENT_LLM", "doubao") or "doubao").strip().lower()
    # provider = (os.getenv("EDUAGENT_LLM", "qwen") or "qwen").strip().lower()

    # 统一的可选覆盖（命令行会写到这里）
    override_model = (os.getenv("EDUAGENT_LLM_MODEL") or "").strip()
    override_base = (os.getenv("EDUAGENT_LLM_BASE_URL") or "").strip()

    if provider in ("deepseek", "ds"):
        ensure_any_env_key(["DEEPSEEK_API_KEY"], required=True, alias="DEEPSEEK_API_KEY")
        model = override_model or get_cfg_or_env(["DEEPSEEK_MODEL"], default="deepseek-reasoner")
        return provider, model, "", ChatDeepSeek(
            model=model,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,

        )

    if provider in ("qwen", "tongyi", "qw"):
        api_key = ensure_any_env_key(
            ["QWEN_API_KEY", "DASHSCOPE_API_KEY", "TONGYI_API_KEY"],
            required=True,
            alias="QWEN_API_KEY/DASHSCOPE_API_KEY",
        )
        base_url = override_base or get_cfg_or_env(
            ["QWEN_BASE_URL", "DASHSCOPE_BASE_URL"],
            default="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        model = override_model or get_cfg_or_env(["QWEN_MODEL"], default="qwen-max")
        return provider, model, base_url, ChatOpenAI(
            model=model,
            temperature=0,
            max_retries=2,
            api_key=api_key,
            base_url=base_url,
        )

    if provider in ("doubao", "ark", "volcengine", "db"):
        api_key = ensure_any_env_key(
            ["ARK_API_KEY", "DOUBAO_API_KEY", "VOLCENGINE_API_KEY", "VOLC_API_KEY"],
            required=True,
            alias="ARK_API_KEY/DOUBAO_API_KEY",
        )
        base_url = override_base or get_cfg_or_env(
            ["DOUBAO_BASE_URL", "ARK_BASE_URL"],
            default="https://ark.cn-beijing.volces.com/api/v3",
        )
        model = (override_model or get_cfg_or_env(["DOUBAO_MODEL", "ARK_MODEL"], default="doubao-seed-1-8-251228")).strip()
        if not model:
            raise RuntimeError(
                "[fatal] 选择 doubao 时必须指定 Model ID：通过环境变量 DOUBAO_MODEL 或命令行 --llm_model（会写入 EDUAGENT_LLM_MODEL）。"
            )
        return provider, model, base_url, ChatOpenAI(
            model=model,
            temperature=0,
            max_retries=2,
            api_key=api_key,
            base_url=base_url,
        )
    
    if provider in ("kimi", "moonshot"):
        api_key = ensure_any_env_key(
            ["KIMI_API_KEY", "MOONSHOT_API_KEY"],
            required=True,
            alias="KIMI_API_KEY/MOONSHOT_API_KEY",
        )
        base_url = override_base or get_cfg_or_env(
            ["KIMI_BASE_URL", "MOONSHOT_BASE_URL"],
            default="https://api.moonshot.cn/v1",
        )
        model = override_model or get_cfg_or_env(["KIMI_MODEL"], default="kimi-k2-thinking-turbo")
        return provider, model, base_url, ChatOpenAI(
            model=model,
            temperature=0,
            max_retries=2,
            api_key=api_key,
            base_url=base_url,
        )
    
    if provider in ("mimo", "mi", "xiaomi"):
        api_key = ensure_any_env_key(
            ["MIMO_API_KEY", "MI_API_KEY", "XIAOMI_API_KEY"],
            required=True,
            alias="MIMO_API_KEY/MI_API_KEY",
        )
        base_url = override_base or get_cfg_or_env(
            ["MIMO_BASE_URL", "MI_BASE_URL"],
            default="https://api.xiaomimimo.com/v1",
        )
        model = override_model or get_cfg_or_env(["MIMO_MODEL"], default="mimo-v2-flash")
        return provider, model, base_url, ChatOpenAI(
            model=model,
            temperature=0,
            max_retries=2,
            api_key=api_key,
            base_url=base_url,
        )

    raise RuntimeError(f"[fatal] 不支持的 EDUAGENT_LLM={provider}，可选 deepseek/qwen/doubao/kimi/mimo。")


_LLM_PROVIDER, _LLM_MODEL, _LLM_BASE_URL, llm = build_llm()
print(f"[llm] provider={_LLM_PROVIDER} model={_LLM_MODEL}" + (f" base_url={_LLM_BASE_URL}" if _LLM_BASE_URL else ""))


# ========= 工具开关（可通过环境变量控制） =========
# 在 eval_computer_exam_alltypes.py 中通过环境变量设置：
#   EDUAGENT_USE_KB / EDUAGENT_USE_NEWS / EDUAGENT_USE_WEB /
#   EDUAGENT_USE_SEARCHAPI / EDUAGENT_USE_FETCHURL
USE_KB = env_flag("EDUAGENT_USE_KB", True)
USE_NEWS = env_flag("EDUAGENT_USE_NEWS", True)
USE_WEB = env_flag("EDUAGENT_USE_WEB", True)
USE_SEARCHAPI = env_flag("EDUAGENT_USE_SEARCHAPI", True)
USE_FETCHURL = env_flag("EDUAGENT_USE_FETCHURL", True)

# ========= 工具构建 =========
tools = []

# ----- 知识库检索（可关闭） -----
kb_tool = None
if USE_KB:
    embed = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        encode_kwargs={"normalize_embeddings": True}
    )
    vs = FAISS.load_local(
        "kb_store/faiss_bge_m3",
        embed,
        allow_dangerous_deserialization=True
    )
    retriever = vs.as_retriever(search_kwargs={"k": 4})
    kb_tool = create_retriever_tool(
        retriever,
        name="kb_search",
        description="在本地知识库中检索与用户问题强相关的片段，用于私有资料问答与引用。",
    )
    tools.append(kb_tool)

# ----- Tavily：新闻搜索（可关闭） -----
news_today_tool = None
if USE_NEWS:
    tavily_key = ensure_env_key("TAVILY_API_KEY", required=True)
    news_today_tool = TavilySearch(
        max_results=8,
        topic="news",           # 关键：新闻通道
        time_range="day",       # 时效：限制为"最近一天"
        search_depth="advanced",
        include_answer=True,
        include_raw_content=False,
        tavily_api_key=tavily_key,
        name="news_search",  # 唯一名称
        description="搜索当天最新的计算机与教育相关新闻资讯、突发通知"
    )
    tools.append(news_today_tool)

# ----- Tavily：通用 Web 搜索（可关闭） -----
web_search_tool = None
if USE_WEB:
    tavily_key = ensure_env_key("TAVILY_API_KEY", required=True)
    web_search_tool = TavilySearch(
        max_results=6,
        topic="general",
        time_range="week",      # 时效下限
        search_depth="basic",
        include_answer=False,
        include_raw_content=False,
        tavily_api_key=tavily_key,
        name="web_search",  # 唯一名称
        description="通用网页搜索，用于查找技术资料、文档等非新闻类信息"
    )
    tools.append(web_search_tool)

# ----- SearchAPI 工具（可关闭） -----
search = SearchApiAPIWrapper()


@tool("searchapi_search", return_direct=False)
def searchapi_search(query: str) -> str:
    """使用 SearchAPI 进行通用网页搜索。输入自然语言查询，返回搜索结果摘要。"""
    return search.run(query)


if USE_SEARCHAPI:
    tools.append(searchapi_search)

# ----- 抓取网页正文（可关闭） -----
@tool("fetch_url", return_direct=False)
def fetch_url(url: str) -> str:
    """抓取指定 URL 的正文并提炼主要内容，用于进一步回答与引用。"""
    try:
        r = requests.get(url, timeout=25, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        doc = Document(r.text)
        html = doc.summary()
        text = BeautifulSoup(html, "html.parser").get_text(" ")
        return text[:8000]
    except Exception as e:
        return f"[fetch_failed] {e}"

if USE_FETCHURL:
    tools.append(fetch_url)

# 为后面构造提示词准备一些标志
HAS_KB = USE_KB and (kb_tool is not None)
HAS_WEB = any([USE_NEWS, USE_WEB, USE_SEARCHAPI, USE_FETCHURL])  # 有任意网页相关工具即可视为有 Web


# ========= 系统提示词（根据工具开关动态适配） =========
def build_system_prompt() -> str:
    lines = []
    lines.append(
        "你是一名面向【职业技术学院计算机学科教育】的课程教学问答智能体。"
        "你的职责是：围绕计算机基础、程序设计、数据结构与算法、操作系统、计算机网络、"
        "数据库、Web/移动开发、软件工程、云计算与DevOps、AI与数据分析、教学组织与评价等主题，"
        "为教师和学生提供**准确、可溯源、可操作**的答复与示例。"
    )

    # -------- 知识来源优先级 --------
    lines.append("")
    lines.append("【知识来源优先级】")

    if HAS_KB:
        lines.append("1) **本地知识库（kb_search）优先**")
        lines.append("   - 该库包含课程章节、教学目标、知识点、实训说明、评价Rubric、案例与模板。")
        lines.append("   - 对“课程教学问答/教学设计/知识点解释/实践步骤/作业与项目规范”等，优先检索本地知识库并引用。")

    if HAS_WEB:
        idx = 2 if HAS_KB else 1
        lines.append(f"{idx}) **网页检索与在线资料**")
        web_desc = []
        if USE_NEWS:
            web_desc.append("`news_today_tool`：当天计算机与教育相关资讯、突发通知；")
        if USE_WEB:
            web_desc.append("`web_search_tool`：通用技术资料与文档；")
        if USE_SEARCHAPI:
            web_desc.append("`searchapi_search`：补充长尾网页检索；")
        if USE_FETCHURL:
            web_desc.append("`fetch_url`：抓取 URL 正文并提炼主要内容。")
        if web_desc:
            # 合并为一两行说明
            lines.append("   - 当本地信息不足，或问题涉及**最新框架版本变更、近一周的技术新闻、第三方库用法**时，再调用网页工具。")
            lines.append("   - " + " ".join(web_desc))
    if (not HAS_KB) and (not HAS_WEB):
        lines.append("1) 当前环境下**不具备外部检索工具**，你只能基于自身已有的通用知识与题目内容进行推理与作答。")

    # -------- 检索与工具使用原则 --------
    lines.append("")
    lines.append("【检索与工具使用原则】")
    if HAS_KB and HAS_WEB:
        lines.append("- 采用“先知识库→后网页”的两阶段策略；搜索关键词尽量具体，加入课程名/技术名/版本号/关键术语。")
    elif HAS_KB and (not HAS_WEB):
        lines.append("- 优先使用本地知识库进行检索；在知识库召回不足时，基于已知内容进行合理推理并清晰说明不确定性。")
    elif (not HAS_KB) and HAS_WEB:
        lines.append("- 直接使用网页工具进行检索；搜索关键词尽量具体，加入课程名/技术名/版本号/关键术语。")
    else:
        lines.append("- 不具备检索工具时，严禁假装调用检索；只能基于已有知识推理，如不确定应明确说明。")

    if HAS_WEB or HAS_KB:
        lines.append("- 不为无关或可直接推导的问题滥用外部搜索；如确需多次检索时，应合并结果、去重归纳。")
        lines.append("- 返回内容务必**附来源标注**：")
        if HAS_KB:
            lines.append("  - 知识库：〔KB｜条目或章节名｜chunk_id/标题〕")
        if HAS_WEB:
            lines.append("  - 网页：〔网页标题｜URL〕")
    else:
        lines.append("- 明确告知用户你无法访问外部资料，只能给出基于现有知识的参考性回答。")

    # -------- 回答结构 --------
    lines.append("")
    lines.append("【回答结构（建议模板）】")
    lines.append("1. **结论速览**（2–4 句，直接回答问题）")
    lines.append("2. **核心知识点/原理**（精炼定义、要点列表）")
    lines.append("3. **步骤与示例**（给出可执行步骤；涉及代码时附**最小可运行示例**与关键注释）")
    lines.append("4. **常见错误与排查**（坑点、复杂度/安全性/边界条件）")
    lines.append("5. **延伸与实践**（课程/实训如何落地、评价要点、与其他知识的衔接）")
    if HAS_KB or HAS_WEB:
        lines.append("6. **来源与进一步阅读**（引用 KB 与网页出处）")

    # -------- 代码与示例风格 --------
    lines.append("")
    lines.append("【代码与示例风格】")
    lines.append("- 示例要**可运行、可复现、最小化**；必要时提供输入输出样例与测试用例。")
    lines.append("- 指明复杂度（时间/空间）与适用场景；涉及命令行/脚本操作，标注系统与版本前提。")
    lines.append("- 涉及数据库/网络/系统操作时，给出**安全注意**与**回滚/恢复**方案。")
    lines.append("- 教学需要时可提供多语言对照（如 C/Python/SQL/JavaScript），但保持简洁。")

    # -------- 教学与学术规范 --------
    lines.append("")
    lines.append("【教学与学术规范】")
    lines.append("- 避免直接给出整份可抄袭的作业/考试答案；如用户明确要求完整解法，应**先给思路与关键步骤**，再给可运行参考实现，并提醒**独立思考与学术诚信**。")
    lines.append("- 不编造不可验证的资料；不确定就明确说明并给出查证路径。")
    lines.append("- 涉及潜在风险的内容（如渗透测试、破坏性脚本）应给出**合法合规与边界**提示，仅在**教学与授权环境**中演示。")

    # -------- 语气与格式 --------
    lines.append("")
    lines.append("【语气与格式】")
    lines.append("- 专业、友好、层次清晰；用标题/列表/代码块组织内容。")
    lines.append("- 术语首次出现时可加**粗体**或括号解释。")
    lines.append("- 重要结论与注意事项可使用“👉 提示”或“⚠ 注意”高亮。")

    # -------- 示例引用格式（按实际启用情况） --------
    lines.append("")
    lines.append("【示例引用格式】")
    if HAS_KB:
        lines.append("- KB 引用示例：〔KB｜数据库技术与应用｜CSK-DB-CH4〕")
    if HAS_WEB:
        lines.append("- 网页引用示例：〔PostgreSQL 16 Docs｜https://www.postgresql.org/docs/16/index.html〕")
    if (not HAS_KB) and (not HAS_WEB):
        lines.append("- 当前环境下无 KB 与网页检索示例，你可以省略具体来源标注，但需明确区分“已有知识”与“猜测/推断”。")

    lines.append("请严格遵循以上规则开展对话、检索与生成（如某类工具未启用，则不要假装使用该工具）。")

    # ========= 新增：图书馆座位预约系统数据库设计试题样例 =========
    lines.append("")
    lines.append("# 试题回答样例")
    lines.append("## 试题：大学图书馆座位预约系统数据库设计")
    lines.append("")
    lines.append("**问题描述**")
    lines.append("某大学图书馆需要开发一个座位预约管理系统，要求支持以下功能：")
    lines.append("")
    lines.append("1. 图书馆有多个楼层，每个楼层有多个区域（如自习区、讨论区、静音区）")
    lines.append("2. 每个区域有多个座位，座位有不同类型（普通座位、带电脑座位、小组讨论桌）")
    lines.append("3. 学生可以预约未来7天内的座位，每次预约时长为1-4小时")
    lines.append("4. 每个学生每天最多可预约2个时间段")
    lines.append("5. 需要记录学生的预约、签到、签退时间（超时15分钟未签到自动取消预约）")
    lines.append("6. 系统需要支持座位状态管理（可用、维修中、已预约、使用中）")
    lines.append("7. 一个学生在同一时间段只能预约一个座位")
    lines.append("8. 每个座位在同一时间段只能被一个学生预约")
    lines.append("")
    lines.append("请设计该系统的关系型数据库表结构，至少包含：")
    lines.append("")
    lines.append("- 列出所有必要的表（至少6个表）")
    lines.append("- 每个表的主键、外键和关键字段")
    lines.append("- 简要说明表之间的关系")
    lines.append("- 用SQL语句创建包含关键约束的预约表")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 思维链提示样例")
    lines.append("")
    lines.append("### 第一步：理解需求，提取实体")
    lines.append("")
    lines.append("从问题描述中识别出核心实体：")
    lines.append("")
    lines.append("1. **学生**（Student）- 系统用户")
    lines.append("2. **图书馆楼层**（Floor）- 物理位置层级")
    lines.append("3. **区域**（Area）- 功能分区（自习区、讨论区等）")
    lines.append("4. **座位**（Seat）- 可预约的最小单位")
    lines.append("5. **预约记录**（Reservation）- 学生与座位的预约关系")
    lines.append("6. **预约时间段**（TimeSlot）- 系统支持的时间分段")
    lines.append("")
    lines.append("### 第二步：分析属性与关系")
    lines.append("")
    lines.append("- 楼层与区域：一对多（一个楼层有多个区域）")
    lines.append("- 区域与座位：一对多（一个区域有多个座位）")
    lines.append("- 学生与预约：一对多（一个学生可以有多个预约记录）")
    lines.append("- 座位与预约：一对多（一个座位可以有多个预约记录）")
    lines.append("- 时间段与预约：一对多（一个时间段可以有多个预约）")
    lines.append("- 预约表需要同时关联学生、座位和时间段")
    lines.append("")
    lines.append("### 第三步：设计表结构")
    lines.append("")
    lines.append("**1. 学生表（student）**")
    lines.append("")
    lines.append("```")
    lines.append("student_id    (主键，学号)")
    lines.append("name          (姓名)")
    lines.append("phone         (联系方式，唯一)")
    lines.append("email         (邮箱，唯一)")
    lines.append("major         (专业)")
    lines.append("credit_score  (信用分，用于限制违约用户)")
    lines.append("created_at    (注册时间)")
    lines.append("```")
    lines.append("")
    lines.append("**2. 楼层表（floor）**")
    lines.append("")
    lines.append("```")
    lines.append("floor_id      (主键)")
    lines.append("floor_number  (楼层号，如1、2、3)")
    lines.append("description   (楼层描述)")
    lines.append("open_time     (开放时间，如'08:00:00')")
    lines.append("close_time    (关闭时间，如'22:00:00')")
    lines.append("```")
    lines.append("")
    lines.append("**3. 区域表（area）**")
    lines.append("")
    lines.append("```")
    lines.append("area_id       (主键)")
    lines.append("floor_id      (外键，引用floor表)")
    lines.append("area_name     (区域名称，如'静音自习区')")
    lines.append("area_type     ('quiet', 'discussion', 'computer')")
    lines.append("max_capacity  (最大容纳人数)")
    lines.append("```")
    lines.append("")
    lines.append("**4. 座位表（seat）**")
    lines.append("")
    lines.append("```")
    lines.append("seat_id       (主键)")
    lines.append("area_id       (外键，引用area表)")
    lines.append("seat_number   (座位编号，如'A01')")
    lines.append("seat_type     ('normal', 'computer', 'group')")
    lines.append("status        ('available', 'reserved', 'in_use', 'maintenance')")
    lines.append("has_power     (是否有电源，布尔)")
    lines.append("has_light     (是否有台灯，布尔)")
    lines.append("```")
    lines.append("")
    lines.append("**5. 时间段表（time_slot）**")
    lines.append("")
    lines.append("```")
    lines.append("slot_id       (主键)")
    lines.append("date          (日期，YYYY-MM-DD)")
    lines.append("start_time    (开始时间，如'09:00:00')")
    lines.append("end_time      (结束时间，如'12:00:00')")
    lines.append("duration      (时长，单位：分钟)")
    lines.append("```")
    lines.append("")
    lines.append("**6. 预约记录表（reservation）**")
    lines.append("")
    lines.append("```")
    lines.append("reservation_id (主键)")
    lines.append("student_id     (外键)")
    lines.append("seat_id        (外键)")
    lines.append("slot_id        (外键)")
    lines.append("reserved_at    (预约时间)")
    lines.append("checkin_time   (签到时间，可空)")
    lines.append("checkout_time  (签退时间，可空)")
    lines.append("status         ('reserved', 'checked_in', 'completed', 'cancelled', 'expired')")
    lines.append("cancelled_at   (取消时间，可空)")
    lines.append("```")
    lines.append("")
    lines.append("### 第四步：考虑约束与优化")
    lines.append("")
    lines.append("- 学生表：`phone`和`email`字段需唯一约束")
    lines.append("- 座位表：`(area_id, seat_number)`组合应唯一，避免重复编号")
    lines.append("- 时间段表：`(date, start_time, end_time)`组合应唯一")
    lines.append("- 预约表：`(student_id, slot_id)`组合应唯一，防止同一学生重复预约")
    lines.append("- 预约表：`(seat_id, slot_id)`组合应唯一，防止座位被重复预约")
    lines.append("- 添加索引：`reservation(student_id, status)`，`reservation(seat_id, slot_id)`")
    lines.append("- 考虑触发器：自动更新座位状态，超时自动取消预约")
    lines.append("")
    lines.append("### 第五步：编写关键SQL")
    lines.append("")
    lines.append("```sql")
    lines.append("-- 创建预约记录表，包含多个约束")
    lines.append("CREATE TABLE reservation (")
    lines.append("    reservation_id INT PRIMARY KEY AUTO_INCREMENT,")
    lines.append("    student_id VARCHAR(20) NOT NULL,")
    lines.append("    seat_id INT NOT NULL,")
    lines.append("    slot_id INT NOT NULL,")
    lines.append("    reserved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,")
    lines.append("    checkin_time TIMESTAMP NULL,")
    lines.append("    checkout_time TIMESTAMP NULL,")
    lines.append("    status ENUM('reserved', 'checked_in', 'completed', 'cancelled', 'expired') DEFAULT 'reserved',")
    lines.append("    cancelled_at TIMESTAMP NULL,")
    lines.append("    -- 外键约束")
    lines.append("    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,")
    lines.append("    FOREIGN KEY (seat_id) REFERENCES seat(seat_id) ON DELETE CASCADE,")
    lines.append("    FOREIGN KEY (slot_id) REFERENCES time_slot(slot_id) ON DELETE CASCADE,")
    lines.append("    -- 防止同一学生在同一时间段重复预约")
    lines.append("    UNIQUE KEY unique_student_slot (student_id, slot_id),")
    lines.append("    -- 防止同一座位在同一时间段被重复预约")
    lines.append("    UNIQUE KEY unique_seat_slot (seat_id, slot_id),")
    lines.append("    -- 为常用查询创建索引")
    lines.append("    INDEX idx_student_status (student_id, status),")
    lines.append("    INDEX idx_seat_status (seat_id, status),")
    lines.append("    INDEX idx_reservation_time (reserved_at),")
    lines.append("    INDEX idx_checkin_status (checkin_time, status)")
    lines.append(");")
    lines.append("")
    lines.append("-- 示例：创建触发器，预约时自动更新座位状态")
    lines.append("DELIMITER $$")
    lines.append("CREATE TRIGGER update_seat_status_on_reserve")
    lines.append("AFTER INSERT ON reservation")
    lines.append("FOR EACH ROW")
    lines.append("BEGIN")
    lines.append("    UPDATE seat SET status = 'reserved' WHERE seat_id = NEW.seat_id;")
    lines.append("END$$")
    lines.append("DELIMITER ;")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 思维链总结")
    lines.append("")
    lines.append("1. **需求分析 → 2. 实体提取 → 3. 关系建模 → 4. 属性设计 → 5. 约束优化 → 6. SQL实现**")
    lines.append("这种结构化思维链适用于数据库设计类问题：")
    lines.append("- **需求分析**：明确业务规则和约束条件")
    lines.append("- **实体提取**：识别系统中的核心对象")
    lines.append("- **关系建模**：确定实体间的关系（1:1, 1:n, n:m）")
    lines.append("- **属性设计**：为每个实体设计合适的字段")
    lines.append("- **约束优化**：考虑数据完整性、性能优化")
    lines.append("- **SQL实现**：将设计转化为可执行的DDL语句")
    lines.append("")


    return "\n".join(lines)


SYSTEM = build_system_prompt()

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])


class DeepSeekThinkingAgentExecutor(AgentExecutor):
    """适配 DeepSeek 思考模式的 Agent Executor"""

    def _construct_scratchpad(
            self, intermediate_steps: List[Tuple[AgentAction, str]]
    ) -> List[Dict[str, Any]]:
        """构建适合 DeepSeek 思考模式的 agent_scratchpad"""
        thoughts = []
        for action, observation in intermediate_steps:
            # 添加思考内容
            thoughts.append({
                "role": "assistant",
                "content": action.log,
                "reasoning_content": action.log  # DeepSeek 需要的字段
            })
            # 添加工具调用结果
            thoughts.append({
                "role": "tool",
                "content": observation,
                "tool_call_id": getattr(action, 'tool_call_id', 'call_1')
            })
        return thoughts

# ========= Agent / Executor =========
if tools:
    print(f"[debug] 已加载的工具列表:")
    for i, tool in enumerate(tools):
        print(f"  [{i}] {tool.name}: {getattr(tool, 'description', '无描述')}")

    # 有工具：构建 Tool Agent
    agent = create_openai_tools_agent(llm, tools, prompt)
    if _LLM_PROVIDER == "deepseek" and "deepseek-reasoner" in _LLM_MODEL.lower():
        executor = DeepSeekThinkingAgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=5,  # 增加最大迭代次数
        )
    else:
        executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=5,  # 增加最大迭代次数
        )
else:
    # 没有任何工具：退化为简单 LLM 链，但对外仍暴露 executor.invoke 接口
    class SimpleExecutor:
        def __init__(self, llm_, prompt_):
            self.llm = llm_
            self.prompt = prompt_

        def invoke(self, inputs: dict):
            # inputs 期望包含 "input" 和 "chat_history"
            _in = dict(inputs or {})
            _in.setdefault("chat_history", [])
            _in.setdefault("agent_scratchpad", [])
            messages = self.prompt.format_messages(**_in)
            resp = self.llm.invoke(messages)
            text = getattr(resp, "content", str(resp))
            return {"output": text}

    executor = SimpleExecutor(llm, prompt)


# ========= 交互入口 =========
if __name__ == "__main__":
    print(f"LangChain Agent Ready！provider={_LLM_PROVIDER} model={_LLM_MODEL}" + (f" base_url={_LLM_BASE_URL}" if _LLM_BASE_URL else "") + " (Ctrl+C 退出)")
    chat_history = []
    try:
        while True:
            q = input("\nYou> ").strip()
            q = clean_text(q)
            if not q:
                continue
            out = executor.invoke({"input": q, "chat_history": chat_history})
            print("\nRAEA>", out["output"])

            # 分析中间步骤
            if "intermediate_steps" in out:
                print(f"\n{'=' * 60}")
                print("📊 工具使用分析:")
                print('=' * 60)

                steps = out["intermediate_steps"]
                print(f"总共执行了 {len(steps)} 个工具步骤:")

                for i, step in enumerate(steps, 1):
                    tool_name = step[0].tool if hasattr(step[0], 'tool') else str(step[0])
                    tool_input = step[0].tool_input if hasattr(step[0], 'tool_input') else str(step[0])
                    tool_output = step[1][:200] + "..." if len(str(step[1])) > 200 else step[1]

                    print(f"\n步骤 {i}:")
                    print(f"  🛠️  工具: {tool_name}")
                    print(f"  📝 输入: {tool_input}")
                    print(f"  📄 输出: {tool_output}")

                # 统计工具使用频率
                tool_counts = {}
                for step in steps:
                    tool_name = step[0].tool if hasattr(step[0], 'tool') else str(step[0])
                    tool_counts[tool_name] = tool_counts.get(tool_name, 0) + 1

                print(f"\n📈 工具使用统计:")
                for tool, count in tool_counts.items():
                    print(f"  {tool}: {count}次")

            chat_history.extend([("human", q), ("ai", out["output"])])
    except KeyboardInterrupt:
        print("\nBye")