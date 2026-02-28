#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题型：
- single_choice: 单选题（A/B/C/D 选一）
- true_false: 判断题（option_A=正确, option_B=错误，对应答案 A 或 B）
- multiple_choice: 多选题（答案为若干个 A/B/C/D 组合，例如 "ABCD"、"AC"）
"""

import argparse
import importlib
import importlib.util
import json
import os
import re
import sys
import time
import hashlib
from typing import Any, List, Dict, Tuple, Set, Optional

# === 安全识别 RemoteProtocolError ===
try:
    import httpx
except ImportError:
    httpx = None


# ------------------------- 配置文件读取 -------------------------
def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    从 config.json 加载默认配置
    """
    # 默认配置（基于您提供的配置文件格式）
    default_config = {
        "GEMINI_API_KEY": "",
        "SEARCHAPI_API_KEY": "",
        "TAVILY_API_KEY": "",

        "MIMO_API_KEY": "",
        "MIMO_BASE": "https://api.xiaomimimo.com/v1",
        "MIMO_MODEL": "mimo-v2-flash",

        "KIMI_API_KEY": "",
        "KIMI_BASE_URL": "https://api.moonshot.cn/v1",
        "KIMI_MODEL": "kimi-k2-thinking",

        "DOUBAO_API_KEY": "",
        "DOUBAO_BASE_URL": "https://ark.cn-beijing.volces.com/api/v3",
        "DOUBAO_MODEL": "doubao-seed-1-8-251228",

        "QWEN_API_KEY": "",
        "QWEN_BASE_URL": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "QWEN_MODEL": "qwen-max",

        "DEEPSEEK_API_KEY": "",
        "DEEPSEEK_BASE_URL": "https://api.deepseek.com/v1",
        "DEEPSEEK_MODEL": "deepseek-chat",

        "DEFAULT_LLM_PROVIDER": "deepseek"
    }

    if not os.path.exists(config_path):
        print(f"[config] 配置文件 {config_path} 不存在，创建默认配置文件")
        # 创建默认配置文件
        try:
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(default_config, f, ensure_ascii=False, indent=2)
            print(f"[config] 已创建默认配置文件: {config_path}")
            print("[config] 请编辑此文件添加您的 API Key 等信息")
        except Exception as e:
            print(f"[config] 创建配置文件失败: {e}")

        return default_config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        # 确保配置文件包含所有必要的键
        for key, default_value in default_config.items():
            if key not in config:
                config[key] = default_value
                print(f"[config] 配置项 {key} 不存在于配置文件中，使用默认值")

        print(f"[config] 从 {config_path} 加载配置成功")
        return config
    except json.JSONDecodeError as e:
        print(f"[config] 配置文件 {config_path} JSON 格式错误: {e}，使用默认配置")
        return default_config
    except Exception as e:
        print(f"[config] 读取配置文件 {config_path} 失败: {e}，使用默认配置")
        return default_config


def get_llm_provider_config(config: Dict[str, Any], provider_name: str) -> Dict[str, str]:
    """
    获取指定 LLM Provider 的配置
    """
    provider_name = provider_name.upper()

    # 定义 LLM Provider 到配置键的映射
    provider_mapping = {
        "DEEPSEEK": {
            "api_key_key": "DEEPSEEK_API_KEY",
            "base_url_key": "DEEPSEEK_BASE_URL",
            "model_key": "DEEPSEEK_MODEL"
        },
        "QWEN": {
            "api_key_key": "QWEN_API_KEY",
            "base_url_key": "QWEN_BASE_URL",
            "model_key": "QWEN_MODEL"
        },
        "DOUBAO": {
            "api_key_key": "DOUBAO_API_KEY",
            "base_url_key": "DOUBAO_BASE_URL",
            "model_key": "DOUBAO_MODEL"
        },
        "KIMI": {
            "api_key_key": "KIMI_API_KEY",
            "base_url_key": "KIMI_BASE_URL",
            "model_key": "KIMI_MODEL"
        },
        "MIMO": {
            "api_key_key": "MIMO_API_KEY",
            "base_url_key": "MIMO_BASE",
            "model_key": "MIMO_MODEL"
        }
    }

    if provider_name not in provider_mapping:
        print(f"[config] LLM Provider '{provider_name}' 不在支持的列表中，使用 DEEPSEEK 作为备用")
        provider_name = "DEEPSEEK"

    mapping = provider_mapping[provider_name]

    # 从配置中获取对应的值
    api_key = config.get(mapping["api_key_key"], "")
    base_url = config.get(mapping["base_url_key"], "")
    model = config.get(mapping["model_key"], "")

    # 如果某个配置项为空，使用合理的默认值
    if not base_url:
        base_url = f"https://api.{provider_name.lower()}.com/v1"

    if not model:
        model = f"{provider_name.lower()}-chat"

    return {
        "api_key": api_key,
        "base_url": base_url,
        "model": model
    }


# ------------------------- Agent loader -------------------------
def load_agent_runner(agent_mod_or_path: str):
    """
    加载你的智能体：
    - 如果传入是 .py 文件路径，则按文件模块加载
    - 否则按模块名 import
    优先寻找模块中的 `executor`（AgentExecutor），否则寻找 `run_agent` 函数。
    """
    mod = None
    # 作为文件路径加载
    if agent_mod_or_path.endswith(".py") or os.path.sep in agent_mod_or_path:
        path = os.path.abspath(agent_mod_or_path)
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"无法加载文件模块: {agent_mod_or_path}")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
    else:
        # 作为普通模块名加载
        mod = importlib.import_module(agent_mod_or_path)

    # 1) 模块中有 executor（LangChain AgentExecutor）
    if hasattr(mod, "executor"):
        executor = getattr(mod, "executor")

        def runner(q: str) -> str:
            out = executor.invoke({"input": q, "chat_history": []})
            if isinstance(out, dict):
                for k in ("output", "result", "final_output", "text"):
                    if k in out:
                        return str(out[k])
            return str(out)

        return runner

    # 2) 模块中有 run_agent 函数
    if hasattr(mod, "run_agent"):
        return getattr(mod, "run_agent")

    raise RuntimeError("在模块/文件中未找到 `executor` 或 `run_agent`。")


def list_agent_tools(mod) -> List[str]:
    tools = []

    if hasattr(mod, "tools") and isinstance(getattr(mod, "tools"), list):
        for t in mod.tools:
            tools.append(getattr(t, "name", None) or getattr(t, "__name__", None) or str(t))

    if hasattr(mod, "executor"):
        ex = mod.executor
        if hasattr(ex, "tools") and isinstance(getattr(ex, "tools"), list):
            for t in ex.tools:
                tools.append(getattr(t, "name", None) or str(t))
        if hasattr(ex, "agent") and hasattr(ex.agent, "tools") and isinstance(getattr(ex.agent, "tools"), list):
            for t in ex.agent.tools:
                tools.append(getattr(t, "name", None) or str(t))

    seen, uniq = set(), []
    for x in tools:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
    return uniq


# ------------------------- 分类评估工具 -------------------------
def macro_f1(labels: List[str], preds: List[str], classes: List[str]) -> float:
    f1s = []
    for c in classes:
        tp = sum(1 for y, p in zip(labels, preds) if y == c and p == c)
        fp = sum(1 for y, p in zip(labels, preds) if y != c and p == c)
        fn = sum(1 for y, p in zip(labels, preds) if y == c and p != c)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        f1s.append(f1)
    return sum(f1s) / len(f1s) if f1s else 0.0


def confusion_matrix(labels: List[str], preds: List[str], classes: List[str]):
    idx = {c: i for i, c in enumerate(classes)}
    m = [[0 for _ in classes] for _ in classes]
    for y, p in zip(labels, preds):
        if y in idx and p in idx:
            m[idx[y]][idx[p]] += 1
    return m


# ------------------------- 归一化工具（关键修复在这里） -------------------------
def _last_nonempty_line(text: str) -> str:
    lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    return lines[-1] if lines else ""


def normalize_single_choice(text: str) -> str:
    """
    单选题：强制映射为 A/B/C/D 中的一个。

    修复点：
    - 旧版用 re.search() 取到全文"第一个"独立字母，很容易被解释里的 "B." 误导
    - 新版优先取"最后一行"的严格答案；否则取全文里"最后一个候选"字母
    """
    if not text:
        return "C"  # 默认猜 C

    raw = str(text)

    # 1) 最后一行严格答案：只允许 A/B/C/D（可带一个 '.' 或 ')'）
    last = _last_nonempty_line(raw)
    m = re.fullmatch(r"(?i)\s*([ABCD])\s*[\.\)]?\s*", last)
    if m:
        return m.group(1).upper()

    # 2) 清理一些常见复述（降低误抓）
    t = raw
    t = t.replace("A/B/C/D", " ").replace("A、B、C、D", " ").replace("A,B,C,D", " ").replace("A B C D", " ")

    candidates: List[str] = []

    # (a) 强信号：答案/最终答案/因此/所以/选择 + 字母
    for mm in re.finditer(r"(?i)(答案|最终答案|因此|所以|选择)\s*[:：]?\s*([ABCD])\b", t):
        candidates.append(mm.group(2).upper())

    # (b) 括号包裹 (A)
    for mm in re.finditer(r"(?i)[\(\[\{]\s*([ABCD])\s*[\)\]\}]", t):
        candidates.append(mm.group(1).upper())

    # (c) A. / B) / option C.
    for mm in re.finditer(r"(?i)\b(option|choice)?\s*([ABCD])\s*[\.\)]\b", t):
        candidates.append(mm.group(2).upper())

    # (d) 弱信号：独立字母（取最后一个）
    for mm in re.finditer(r"(?i)\b([ABCD])\b", t):
        candidates.append(mm.group(1).upper())

    if candidates:
        return candidates[-1]

    return "C"


def normalize_true_false(text: str) -> str:
    """
    判断题：答案只允许 A/B。
    约定：
      - A: 正确
      - B: 错误

    修复点同上：优先取最后一行，否则取全文最后一个候选
    """
    if not text:
        return "B"  # 默认保守为"错误"

    raw = str(text)

    # 1) 最后一行严格答案
    last = _last_nonempty_line(raw)
    m = re.fullmatch(r"(?i)\s*([AB])\s*[\.\)]?\s*", last)
    if m:
        return m.group(1).upper()

    # 2) 全文最后一个 A/B 候选
    candidates = [mm.group(1).upper() for mm in re.finditer(r"(?i)\b([AB])\b", raw)]
    if candidates:
        return candidates[-1]

    # 3) 关键词兜底
    t_simple = raw.lower()
    if any(k in t_simple for k in ["正确", "对", "true", "yes"]):
        return "A"
    if any(k in t_simple for k in ["错误", "不对", "false", "no"]):
        return "B"

    return "B"


def normalize_multi_choice(text: str) -> str:
    """
    多选题归一化：
    优先级：
    1) 取最后一行非空文本，如果该行主要由 ABCD 构成，则抽取其中所有 A/B/C/D，去重+排序；
    2) 若最后一行抓不到，从全文兜底抓；
    3) 仍无则默认 'ABCD'
    """
    if not text:
        return "ABCD"

    raw = str(text).strip()
    if not raw:
        return "ABCD"

    # 清理常见复述
    t_full = raw.upper()
    t_full = t_full.replace("A/B/C/D", " ").replace("A、B、C、D", " ").replace("A,B,C,D", " ").replace("A B C D", " ")

    # 1) 最后一行
    last = _last_nonempty_line(raw).strip().upper()
    # 如果最后一行是类似 "AC" / "ABCD" / "A C" / "A,C" 这种，抽取即可
    letters = re.findall(r"[ABCD]", last)
    letters = sorted(set(letters))
    if letters:
        # 额外约束：最后一行里不能出现太多其它字母数字（避免解释尾巴误抓）
        # 这个约束比较松：只要含 ABCD 就收；你想更严可以加更强的 fullmatch
        return "".join(letters)

    # 2) 兜底全文
    letters = re.findall(r"[ABCD]", t_full)
    letters = sorted(set(letters))
    if letters:
        return "".join(letters)

    return "ABCD"


# ------------------------- 唯一 key & 断点续跑 -------------------------
def make_key(question: str, gold: str, dataset_name: str = "") -> str:
    combined = f"{dataset_name}|||{(question or '')}|||{(gold or '')}"
    return hashlib.sha1(combined.encode("utf-8")).hexdigest()


def load_existing_preds(save_path: str) -> Tuple[Set[str], List[Dict[str, Any]]]:
    processed_keys: Set[str] = set()
    loaded_records: List[Dict[str, Any]] = []

    if not os.path.exists(save_path):
        return processed_keys, loaded_records

    try:
        with open(save_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    q = rec.get("question", "")
                    gold = rec.get("gold", "") or rec.get("gold_answer", "")
                    ds = rec.get("dataset", "computer_exam")
                    key = make_key(q, gold, ds)
                    processed_keys.add(key)
                    loaded_records.append(rec)
                except Exception as e:
                    print(f"[warn] 解析历史结果第 {i} 行失败: {e} -- 已跳过")
    except Exception as e:
        print(f"[warn] 无法打开历史结果文件 {save_path}: {e}")

    return processed_keys, loaded_records


# ------------------------- 提示词构造 -------------------------
def build_single_prompt(question: str, options: Dict[str, str]) -> str:
    optA = options.get("option_A", "").strip()
    optB = options.get("option_B", "").strip()
    optC = options.get("option_C", "").strip()
    optD = options.get("option_D", "").strip()

    lines = [
        "你是一名职业技术学院计算机学科教学助手。",
        "下面是一道【单项选择题】，请从 A、B、C、D 四个选项中选择一个最合适的答案，",
        "并且【严格只输出一个大写字母】作为最终答案。",
        "",
        f"题目：{question}",
        "",
        "选项：",
        f"A. {optA}",
        f"B. {optB}",
        f"C. {optC}",
        f"D. {optD}",
        "",
        "请只输出一个大写字母 A、B、C 或 D，不要输出任何其它内容。"
    ]
    return "\n".join(lines)


def build_true_false_prompt(question: str, options: Dict[str, str]) -> str:
    optA = options.get("option_A", "").strip() or "正确"
    optB = options.get("option_B", "").strip() or "错误"

    lines = [
        "你是一名职业技术学院计算机学科教学助手。",
        "下面是一道【判断题】。",
        "约定：",
        "  - 选项 A 表示正确",
        "  - 选项 B 表示错误",
        "请根据题意判断正确或错误，并【严格只输出一个大写字母 A 或 B】作为最终答案。",
        "",
        f"题目：{question}",
        "",
        "选项：",
        f"A. {optA}",
        f"B. {optB}",
        "",
        "请只输出一个大写字母 A 或 B，不要输出任何其它内容。"
    ]
    return "\n".join(lines)


def build_multi_prompt(question: str, options: Dict[str, str]) -> str:
    optA = options.get("option_A", "").strip()
    optB = options.get("option_B", "").strip()
    optC = options.get("option_C", "").strip()
    optD = options.get("option_D", "").strip()

    lines = [
        "你是一名职业技术学院计算机学科教学助手。",
        "下面是一道【多项选择题】。",
        "请从 A、B、C、D 中选择一个或多个正确选项。",
        "",
        "答题要求：",
        "  - 若只有 A 和 C 正确，请输出 AC。",
        "  - 若 A、B、C、D 都正确，请输出 ABCD。",
        "  - 不要包含空格、顿号、逗号或其他符号。",
        "  - 不要输出除 A/B/C/D 外的任何字符。",
        "",
        f"题目：{question}",
        "",
        "选项：",
        f"A. {optA}",
        f"B. {optB}",
        f"C. {optC}",
        f"D. {optD}",
        "",
        "请先自行分析，但**最终答案必须单独写在最后一行**。",
        "最后一行请严格只输出若干个大写字母 A、B、C、D 组成的字符串，例如：A、AC、BCD、ABCD。"
    ]
    return "\n".join(lines)


# ------------------------- 数据加载 -------------------------
def load_computer_exam_dataset(jsonl_path: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    total_raw = 0

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total_raw += 1
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"[warn] 第 {total_raw} 行 JSON 解析失败: {e} -- 已跳过")
                continue

            qtype = (obj.get("type") or "").strip()
            qtype_lower = qtype.lower()
            q = (obj.get("question") or "").strip()
            raw_answer = str(obj.get("answer") or "").strip().upper()
            options = {
                "option_A": (obj.get("option_A") or "").strip(),
                "option_B": (obj.get("option_B") or "").strip(),
                "option_C": (obj.get("option_C") or "").strip(),
                "option_D": (obj.get("option_D") or "").strip(),
            }

            if not q or not raw_answer:
                continue

            if qtype_lower == "single_choice":
                if raw_answer not in {"A", "B", "C", "D"}:
                    continue
                gold = raw_answer
                prompt_text = build_single_prompt(q, options)

            elif qtype_lower == "true_false":
                if raw_answer not in {"A", "B"}:
                    continue
                gold = raw_answer
                prompt_text = build_true_false_prompt(q, options)

            elif qtype_lower == "multiple_choice":
                letters = [ch for ch in raw_answer if ch in {"A", "B", "C", "D"}]
                if not letters:
                    continue
                gold = "".join(sorted(set(letters)))
                prompt_text = build_multi_prompt(q, options)

            else:
                continue

            rows.append(
                {
                    "id": obj.get("id", ""),
                    "type": qtype_lower,
                    "question": prompt_text,
                    "gold_answer": gold,
                    "raw_question": q,
                    "options": options,
                }
            )

    print(f"[load] 原始行数: {total_raw}, 规范化后的题目数: {len(rows)}")
    type_count: Dict[str, int] = {}
    for r in rows:
        type_count[r["type"]] = type_count.get(r["type"], 0) + 1
    print("[load] 题型分布:", type_count)
    return rows


# ------------------------- 主流程 -------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--dataset_path",
        required=True,
        help="all_computer_exams.jsonl 的路径，例如 ./all_computer_exams.std.jsonl",
    )
    ap.add_argument(
        "--agent_mod",
        required=True,
        help="你的智能体模块名或 .py 文件路径，例如: langchain_agent 或 ./langchain_agent.py",
    )
    ap.add_argument(
        "--max_n",
        type=int,
        default=0,
        help="最多评测多少条（0=全量）",
    )
    ap.add_argument(
        "--save",
        default="results/computer_exam_preds.jsonl",
        help="预测结果保存为 JSONL 的路径",
    )
    ap.add_argument(
        "--resume",
        dest="resume",
        action="store_true",
        default=True,
        help="启用断点续跑（默认开启）",
    )
    ap.add_argument(
        "--no-resume",
        dest="resume",
        action="store_false",
        help="禁用断点续跑（重新覆盖保存文件）",
    )
    ap.add_argument(
        "--debug",
        action="store_true",
        help="调试模式：打印前几条题目与模型输出",
    )

    # LLM Provider 选择
    ap.add_argument(
        "--llm",
        default="",
        help="选择 LLM Provider（如 deepseek, qwen, doubao, kimi, mimo 等）",
    )
    ap.add_argument(
        "--llm_model",
        default="",
        help="可选：覆盖默认模型名/Model ID",
    )
    ap.add_argument(
        "--llm_base_url",
        default="",
        help="可选：覆盖 OpenAI-compatible base_url",
    )
    ap.add_argument(
        "--config",
        default="config.json",
        help="配置文件路径，默认为 config.json",
    )

    # 工具开关（默认启用，用 --no_xx 来禁用）
    ap.add_argument("--no_kb", action="store_true", help="禁用 kb_search 工具")
    ap.add_argument("--no_news", action="store_true", help="禁用 news_today_tool 工具")
    ap.add_argument("--no_web", action="store_true", help="禁用 web_search_tool 工具")
    ap.add_argument("--no_searchapi", action="store_true", help="禁用 searchapi_search 工具")
    ap.add_argument("--no_fetchurl", action="store_true", help="禁用 fetch_url 工具")

    args = ap.parse_args()

    # 1) 加载配置文件
    config = load_config(args.config)

    # 确定要使用的 LLM Provider（命令行参数优先，其次配置文件默认值）
    llm_provider = args.llm.lower() if args.llm else config.get("DEFAULT_LLM_PROVIDER", "deepseek").lower()

    # 获取该 LLM Provider 的配置
    provider_config = get_llm_provider_config(config, llm_provider)

    # 确定最终的配置（命令行参数优先，其次配置文件，最后默认值）
    llm_model = args.llm_model if args.llm_model else provider_config.get("model", "")
    llm_base_url = args.llm_base_url if args.llm_base_url else provider_config.get("base_url", "")
    api_key = provider_config.get("api_key", "")

    # 在导入 agent 之前设置环境变量（默认启用，--no_xxx 覆盖为禁用）
    os.environ.setdefault("EDUAGENT_USE_KB", "1")
    os.environ.setdefault("EDUAGENT_USE_NEWS", "1")
    os.environ.setdefault("EDUAGENT_USE_WEB", "1")
    os.environ.setdefault("EDUAGENT_USE_SEARCHAPI", "1")
    os.environ.setdefault("EDUAGENT_USE_FETCHURL", "1")

    if args.no_kb:
        os.environ["EDUAGENT_USE_KB"] = "0"
    if args.no_news:
        os.environ["EDUAGENT_USE_NEWS"] = "0"
    if args.no_web:
        os.environ["EDUAGENT_USE_WEB"] = "0"
    if args.no_searchapi:
        os.environ["EDUAGENT_USE_SEARCHAPI"] = "0"
    if args.no_fetchurl:
        os.environ["EDUAGENT_USE_FETCHURL"] = "0"

    print("[env] EDUAGENT_USE_KB      =", os.environ.get("EDUAGENT_USE_KB"))
    print("[env] EDUAGENT_USE_NEWS    =", os.environ.get("EDUAGENT_USE_NEWS"))
    print("[env] EDUAGENT_USE_WEB     =", os.environ.get("EDUAGENT_USE_WEB"))
    print("[env] EDUAGENT_USE_SEARCHAPI=", os.environ.get("EDUAGENT_USE_SEARCHAPI"))
    print("[env] EDUAGENT_USE_FETCHURL=", os.environ.get("EDUAGENT_USE_FETCHURL"))

    # 在导入 agent 之前设置 LLM 选择（langchain_agent.py 会读取这些环境变量）
    os.environ["EDUAGENT_LLM"] = llm_provider
    os.environ["EDUAGENT_LLM_MODEL"] = llm_model
    os.environ["EDUAGENT_LLM_BASE_URL"] = llm_base_url
    if api_key:
        os.environ["EDUAGENT_API_KEY"] = api_key

    # 设置其他工具的 API Key
    if "SEARCHAPI_API_KEY" in config and config["SEARCHAPI_API_KEY"]:
        os.environ["SEARCHAPI_API_KEY"] = config["SEARCHAPI_API_KEY"]
    if "TAVILY_API_KEY" in config and config["TAVILY_API_KEY"]:
        os.environ["TAVILY_API_KEY"] = config["TAVILY_API_KEY"]
    if "GEMINI_API_KEY" in config and config["GEMINI_API_KEY"]:
        os.environ["GEMINI_API_KEY"] = config["GEMINI_API_KEY"]

    print("[config] 使用的配置:")
    print(f"[config] LLM Provider       = {llm_provider.upper()}")
    print(f"[config] LLM Model          = {llm_model}")
    print(f"[config] LLM Base URL       = {llm_base_url}")
    print(f"[config] API Key            = {'*' * 8 if api_key else '(未设置)'}")

    # 检查 API Key 是否已设置
    if not api_key:
        print(f"[warning] LLM Provider '{llm_provider.upper()}' 的 API Key 未在配置文件中设置")
        print(f"[warning] 请编辑 {args.config} 文件，在 {llm_provider.upper()}_API_KEY 字段添加您的 API Key")

    # 1) 加载 Agent 运行器
    run_agent = load_agent_runner(args.agent_mod)
    print(f"[info] 成功加载智能体模块: {args.agent_mod}")
    print("[info] agent registered tools:", list_agent_tools(args.agent_mod))

    # 2) 加载数据集
    ds_list = load_computer_exam_dataset(args.dataset_path)
    if not ds_list:
        print("[error] 加载到的样本数为 0，请检查路径及格式。")
        return

    # 3) 断点续跑：读历史预测
    processed_keys, existing_records = set(), []
    if args.resume and os.path.exists(args.save):
        print(f"[resume] 从 {args.save} 读取历史预测记录 ...")
        processed_keys, existing_records = load_existing_preds(args.save)
        print(f"[resume] 历史已处理样本数: {len(processed_keys)}")

    # 分别存储三种题型的标签/预测值
    single_labels: List[str] = []
    single_preds: List[str] = []

    tf_labels: List[str] = []
    tf_preds: List[str] = []

    multi_labels: List[str] = []
    multi_preds: List[str] = []

    all_labels: List[str] = []
    all_preds: List[str] = []

    # 将历史记录纳入统计（注意需要有 q_type 字段才准确）
    for rec in existing_records:
        q_type = rec.get("q_type")
        gold = str(rec.get("gold", "") or rec.get("gold_answer", "")).strip().upper()
        pred = str(rec.get("pred", "")).strip().upper()
        if not gold or not pred:
            continue
        all_labels.append(gold)
        all_preds.append(pred)
        if q_type == "single_choice":
            single_labels.append(gold)
            single_preds.append(pred)
        elif q_type == "true_false":
            tf_labels.append(gold)
            tf_preds.append(pred)
        elif q_type == "multiple_choice":
            multi_labels.append(gold)
            multi_preds.append(pred)

    t0 = time.time()
    total_examples = len(ds_list)

    mode = "a" if (args.resume and os.path.exists(args.save)) else "w"
    f_out = open(args.save, mode, encoding="utf-8")

    PRINT_EVERY = 1
    initial_processed = len(processed_keys)
    processed_this_run = 0

    MAX_AGENT_RETRY = 3

    def is_remote_protocol_error(e: Exception) -> bool:
        if httpx is not None and isinstance(e, httpx.RemoteProtocolError):
            return True
        msg = str(e)
        if "incomplete chunked read" in msg:
            return True
        if "RemoteProtocolError" in e.__class__.__name__:
            return True
        return False

    try:
        for ex in ds_list:
            q_prompt = ex["question"]
            gold = ex["gold_answer"]
            q_type = ex["type"]
            dataset_name = "computer_exam"

            key = make_key(q_prompt, gold, dataset_name)
            if key in processed_keys:
                continue

            if args.max_n and processed_this_run >= args.max_n:
                print(f"[info] 已达到 max_n={args.max_n}，停止本次评测。")
                break

            processed_this_run += 1
            current_index = initial_processed + processed_this_run

            q_preview = ex["raw_question"].replace("\n", " ").strip()
            if len(q_preview) > 80:
                q_preview = q_preview[:77] + "..."
            if (processed_this_run % PRINT_EVERY) == 0:
                print(f"[{current_index}/{total_examples}] ({q_type}) 处理题目: {q_preview}")

            resp: str = ""
            pred: str = ""
            last_err: Optional[Exception] = None
            success = False

            for attempt in range(1, MAX_AGENT_RETRY + 1):
                try:
                    resp = run_agent(q_prompt)
                    success = True
                    break
                except Exception as e:
                    last_err = e
                    is_remote = is_remote_protocol_error(e)
                    print(f"[warn] 调用智能体出错（第 {attempt} 次）: {e}")
                    if attempt < MAX_AGENT_RETRY and is_remote:
                        time.sleep(2)
                        continue
                    else:
                        break

            if not success:
                rec = {
                    "dataset": dataset_name,
                    "q_type": q_type,
                    "id": ex.get("id", ""),
                    "raw_question": ex.get("raw_question", ""),
                    "options": ex.get("options", {}),
                    "question": q_prompt,
                    "gold": gold,
                    "pred": "",
                    "response": f"[ERROR] agent call failed: {repr(last_err)}",
                    "error": repr(last_err) if last_err is not None else "unknown_error",
                }
                f_out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f_out.flush()
                os.fsync(f_out.fileno())
                processed_keys.add(key)
                continue

            # === 正常成功分支：归一化 ===
            if q_type == "single_choice":
                pred = normalize_single_choice(resp)
                single_labels.append(gold)
                single_preds.append(pred)
            elif q_type == "true_false":
                pred = normalize_true_false(resp)
                tf_labels.append(gold)
                tf_preds.append(pred)
            else:
                pred = normalize_multi_choice(resp)
                multi_labels.append(gold)
                multi_preds.append(pred)

            all_labels.append(gold)
            all_preds.append(pred)

            rec = {
                "dataset": dataset_name,
                "q_type": q_type,
                "id": ex.get("id", ""),
                "raw_question": ex.get("raw_question", ""),
                "options": ex.get("options", {}),
                "question": q_prompt,
                "gold": gold,
                "pred": pred,
                "response": resp,
                # 方便你排查：把最后一行也保存下来
                "response_last_line": _last_nonempty_line(resp),
            }
            f_out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f_out.flush()
            os.fsync(f_out.fileno())
            processed_keys.add(key)

            if args.debug and processed_this_run <= 3:
                print("\n--- 调试样本 ---")
                print("题型:", q_type)
                print("题目（原始）:", ex.get("raw_question", ""))
                print("标准答案:", gold)
                print("模型原始输出:", resp)
                print("最后一行:", _last_nonempty_line(resp))
                print("归一化后预测:", pred)
                print("---------------\n")

    finally:
        f_out.close()

    # 5) 汇总指标
    dt = time.time() - t0

    def acc(labels: List[str], preds: List[str]) -> float:
        if not labels:
            return 0.0
        return sum(1 for y, p in zip(labels, preds) if y == p) / len(labels)

    overall_acc = acc(all_labels, all_preds)
    single_acc = acc(single_labels, single_preds)
    tf_acc = acc(tf_labels, tf_preds)
    multi_acc = acc(multi_labels, multi_preds)

    print("\n========== Evaluation on all_computer_exams ==========")
    print(f"Total questions (all types, success only): {len(all_labels)}")
    print(f"Overall Accuracy: {overall_acc:.4f}")
    print("------------------------------------------------------")
    print(f"Single Choice  (single_choice):  N={len(single_labels)}  Acc={single_acc:.4f}")
    print(f"True / False   (true_false):     N={len(tf_labels)}      Acc={tf_acc:.4f}")
    print(f"Multiple Choice(multiple_choice):N={len(multi_labels)}   Acc={multi_acc:.4f}")

    if single_labels:
        single_macro = macro_f1(single_labels, single_preds, ["A", "B", "C", "D"])
        single_cm = confusion_matrix(single_labels, single_preds, ["A", "B", "C", "D"])
        print("\n[Single Choice] Macro-F1 (A/B/C/D): {:.4f}".format(single_macro))
        print("Confusion Matrix (rows=gold, cols=pred) order=[A, B, C, D]")
        for row in single_cm:
            print("  " + "\t".join(str(v) for v in row))

    if tf_labels:
        tf_macro = macro_f1(tf_labels, tf_preds, ["A", "B"])
        tf_cm = confusion_matrix(tf_labels, tf_preds, ["A", "B"])
        print("\n[True/False] Macro-F1 (A/B): {:.4f}".format(tf_macro))
        print("Confusion Matrix (rows=gold, cols=pred) order=[A, B]")
        for row in tf_cm:
            print("  " + "\t".join(str(v) for v in row))

    print(f"\n预测结果已保存/追加到: {args.save}")
    print(f"耗时: {dt:.1f}s")


if __name__ == "__main__":
    main()