#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import os


def iter_json_blocks(json_path: str):
    """
    从一个“连续 JSON 对象”文件中，按花括号匹配出一个个完整 JSON 块。
    支持多行缩进，且会忽略字符串内部的 { }。
    适配你现在这种格式：

    {
      "id": "...",
      ...
    }
    {
      "id": "...",
      ...
    }
    """
    buf_lines = []
    depth = 0
    in_string = False
    escape = False

    with open(json_path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")

            # 如果当前不在对象内部（depth == 0），且这一行是空的，就跳过
            if not line.strip() and depth == 0:
                continue

            buf_lines.append(line)

            # 扫描本行，更新 depth / in_string 状态
            for ch in line:
                if escape:
                    escape = False
                    continue

                if ch == "\\":
                    escape = True
                    continue

                if ch == '"':
                    in_string = not in_string
                    continue

                if not in_string:
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1

            # depth 回到 0，说明一个 JSON 对象结束
            if depth == 0 and buf_lines:
                block = "\n".join(buf_lines).strip()
                if block:
                    try:
                        obj = json.loads(block)
                        yield obj
                    except Exception as e:
                        print(f"[warn] JSON 块解析失败: {e} -- 内容前 80 字符: {block[:80]!r}")
                buf_lines = []

    if depth != 0:
        print(f"[warn] 文件结束时花括号未配对（depth={depth}），可能有残缺的 JSON 对象。")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--input",
        default="all_computer_exams.jsonl",
        help="原始多行 JSON 文件路径（现在这个 all_computer_exams.jsonl）",
    )
    ap.add_argument(
        "--output",
        default="all_computer_exams.std.jsonl",
        help="输出的一行一个 JSON 的 JSONL 文件路径",
    )
    args = ap.parse_args()

    in_path = args.input
    out_path = args.output

    if not os.path.exists(in_path):
        print(f"[error] 输入文件不存在: {in_path}")
        return

    count = 0
    with open(out_path, "w", encoding="utf-8") as fout:
        for obj in iter_json_blocks(in_path):
            json_str = json.dumps(obj, ensure_ascii=False)
            fout.write(json_str + "\n")
            count += 1

    print(f"[done] 解析并写出 JSON 对象数: {count}")
    print(f"[done] 新文件已保存到: {out_path}")
    print("你现在可以在评测脚本里用这个标准 JSONL 文件了。")


if __name__ == "__main__":
    main()
