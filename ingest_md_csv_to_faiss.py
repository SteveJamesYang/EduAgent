from pathlib import Path
from typing import List, Optional, Any, Dict
import argparse
import pandas as pd
import re
import json
import hashlib
from bs4 import BeautifulSoup

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document


# ==================== 新增的哈希和记录函数 ====================
def get_file_hash(file_path):
    """计算文件哈希值"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def load_processed_files(index_dir):
    index_dir.mkdir(parents=True, exist_ok=True)
    record_file = index_dir / "processed_files.json"
    if record_file.exists():
        try:
            with open(record_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("警告: 处理记录文件损坏，将重新创建")
            return {}
    return {}


def save_processed_files(index_dir, processed_dict):
    """保存已处理文件记录"""
    index_dir.mkdir(parents=True, exist_ok=True)
    record_file = index_dir / "processed_files.json"
    # 可选：原子写入，避免写到一半文件损坏
    tmp = record_file.with_suffix(".json.tmp")
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(processed_dict, f, ensure_ascii=False, indent=2)
    tmp.replace(record_file)


# ==================== 结束新增函数 ====================
def norm(v: Any) -> str:
    if pd.isna(v): return ""
    return str(v).strip()


def clean_markdown_content(text: str) -> str:
    """清理Markdown内容，移除过多的格式标记"""
    # 移除HTML标签（如果有）
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()

    # 移除过多的代码块标记（可选）
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)

    # 移除过多的标题标记
    text = re.sub(r'#{1,6}\s*', '', text)

    return text.strip()


def process_markdown_file(path: Path, embed, vs: Optional[FAISS], index_dir: Path,
                          chunk_size: int = 1000, chunk_overlap: int = 200) -> FAISS:
    """处理单个Markdown文件，按内容分块"""
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    print(f"处理Markdown文件: {path.name}")

    try:
        # 读取Markdown文件内容
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 清理内容
        cleaned_content = clean_markdown_content(content)
        if not cleaned_content:
            print(f"警告: 文件 {path.name} 内容为空或清理后无文本")
            return vs

        # 初始化文本分割器
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

        # 分割文本
        chunks = text_splitter.split_text(cleaned_content)

        # 创建文档对象
        documents = []
        for i, chunk in enumerate(chunks):
            if chunk.strip():  # 确保块不为空
                documents.append(Document(
                    page_content=chunk,
                    metadata={
                        "source": path.name,
                        "source_path": str(path),
                        "chunk_index": i,
                        "total_chunks": len(chunks),
                        "file_type": "markdown"
                    }
                ))

        # 添加到向量库
        if not documents:
            print(f"警告: 文件 {path.name} 分割后无有效文档块")
            return vs

        if vs is None:
            vs = FAISS.from_documents(documents, embed)
        else:
            vs.add_documents(documents)

        print(f"✅ Markdown文件 {path.name} 处理完成，生成 {len(documents)} 个文档块")
        return vs

    except Exception as e:
        print(f"❌ 处理Markdown文件 {path.name} 时出错: {e}")
        return vs


def rows_to_documents(df: pd.DataFrame, source_path: Path, columns_to_use: Optional[List[str]]) -> List[Document]:
    cols = columns_to_use or list(df.columns)
    docs: List[Document] = []
    for i, row in df.iterrows():
        parts = []
        for c in cols:
            if c not in df.columns:
                continue
            val = norm(row[c])
            if val:
                parts.append(f"{c}: {val}")
        text = "\n".join(parts)
        if text:
            docs.append(Document(
                page_content=text,
                metadata={
                    "source": source_path.name,
                    "source_path": str(source_path),
                    "sheet": "",  # CSV 无 sheet
                    "row_index": int(i),
                    "columns": cols,
                    "file_type": "csv"
                }
            ))
    return docs


def process_csv(path: Path, embed, vs: Optional[FAISS], index_dir: Path,
                columns_to_use: Optional[List[str]], chunk_rows: int, batch_embed: int) -> FAISS:
    reader = pd.read_csv(path, dtype=str, chunksize=chunk_rows, keep_default_na=True)
    running_vs = vs
    total_rows = 0

    for chunk_idx, df in enumerate(reader, start=1):
        total_rows += len(df)
        for start in range(0, len(df), batch_embed):
            sub = df.iloc[start:start + batch_embed]
            docs = rows_to_documents(sub, source_path=path, columns_to_use=columns_to_use)
            if not docs:
                continue
            if running_vs is None:
                running_vs = FAISS.from_documents(docs, embed)
            else:
                running_vs.add_documents(docs)

        if running_vs:
            running_vs.save_local(str(index_dir))
            print(f"[{path.name}] chunk#{chunk_idx} 累计行: {total_rows} -> 已保存到 {index_dir}")

    return running_vs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir", type=str, default="kb_docs/books", help="输入目录（支持CSV和MD文件）")
    ap.add_argument("--index_dir", type=str, default="kb_store/faiss_bge_m3", help="FAISS 索引输出目录")
    ap.add_argument("--cols", type=str, default="", help="逗号分隔的列名子集（仅对CSV有效）；留空=全部列")
    ap.add_argument("--chunk_rows", type=int, default=20000, help="每次读取的CSV行数")
    ap.add_argument("--batch_embed", type=int, default=2000, help="每批嵌入/写入的文档条数")
    ap.add_argument("--md_chunk_size", type=int, default=1000, help="Markdown文件分块大小")
    ap.add_argument("--md_chunk_overlap", type=int, default=200, help="Markdown文件分块重叠大小")
    args = ap.parse_args()

    data_dir = Path(args.data_dir)
    index_dir = Path(args.index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)
    # index_dir.parent.mkdir(parents=True, exist_ok=True)

    if data_dir.resolve() == index_dir.resolve():
        raise SystemExit(f"❌ data_dir 与 index_dir 不能相同：{data_dir}")

    # 同时查找CSV和MD文件
    csv_files = list(data_dir.rglob("*.csv"))
    md_files = list(data_dir.rglob("*.md"))
    all_files = csv_files + md_files

    print(f"扫描目录: {data_dir}")
    print(f"发现 CSV 文件数: {len(csv_files)}")
    print(f"发现 Markdown 文件数: {len(md_files)}")
    print(f"总文件数: {len(all_files)}")

    if not all_files:
        raise SystemExit("未找到任何CSV或MD文件。请确认文件放在 data_dir 目录中。")

    columns_to_use = [c.strip() for c in args.cols.split(",") if c.strip()] if args.cols else None

    embed = HuggingFaceEmbeddings(model_name="BAAI/bge-m3",
                                  encode_kwargs={"normalize_embeddings": True})

    # 加载已处理文件记录
    processed_files = load_processed_files(index_dir)
    print(f"已记录的处理文件数: {len(processed_files)}")

    vs = None
    if index_dir.exists() and (index_dir / "index.faiss").exists():
        vs = FAISS.load_local(str(index_dir), embed, allow_dangerous_deserialization=True)
        print(f"检测到已有索引 -> {index_dir}，将进行增量追加…")

    processed_count = 0
    skipped_count = 0

    # 处理CSV文件
    for csv_path in csv_files:
        file_hash = get_file_hash(csv_path)
        if str(csv_path) in processed_files:
            if processed_files[str(csv_path)] == file_hash:
                print(f"跳过未修改的CSV文件: {csv_path.name}")
                skipped_count += 1
                continue
            else:
                print(f"CSV文件已修改，重新处理: {csv_path.name}")

        print(f"\n开始处理CSV文件: {csv_path.name}")
        vs = process_csv(csv_path, embed, vs, index_dir, columns_to_use, args.chunk_rows, args.batch_embed)

        # 更新处理记录
        processed_files[str(csv_path)] = file_hash
        save_processed_files(index_dir, processed_files)
        processed_count += 1

    # 处理Markdown文件
    for md_path in md_files:
        file_hash = get_file_hash(md_path)
        if str(md_path) in processed_files:
            if processed_files[str(md_path)] == file_hash:
                print(f"跳过未修改的Markdown文件: {md_path.name}")
                skipped_count += 1
                continue
            else:
                print(f"Markdown文件已修改，重新处理: {md_path.name}")

        print(f"\n开始处理Markdown文件: {md_path.name}")
        vs = process_markdown_file(md_path, embed, vs, index_dir,
                                   args.md_chunk_size, args.md_chunk_overlap)

        # 更新处理记录
        processed_files[str(md_path)] = file_hash
        save_processed_files(index_dir, processed_files)
        processed_count += 1

        # 每次处理完一个MD文件后保存索引
        if vs:
            vs.save_local(str(index_dir))
            print(f"索引已保存到 {index_dir}")

    if vs:
        vs.save_local(str(index_dir))
        print(f"✅ 完成！索引已保存到 {index_dir}")
        print(f"处理统计: 新增 {processed_count} 个文件, 跳过 {skipped_count} 个未修改文件")
        print(f"文件类型: {len(csv_files)} 个CSV文件, {len(md_files)} 个Markdown文件")


if __name__ == "__main__":
    main()