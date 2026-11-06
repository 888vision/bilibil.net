#!/usr/bin/env python3
"""Download a PDF from a URL or safely delete one explicitly named PDF."""

import argparse
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def download_pdf(url: str, output: Path) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SystemExit("请输入有效的 http 或 https 地址。")
    output.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": "pdf-tool/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            data = response.read()
    except Exception as exc:
        raise SystemExit(f"下载失败：{exc}") from exc
    if not data.startswith(b"%PDF-"):
        raise SystemExit("下载内容看起来不是 PDF，未保存文件。")
    output.write_bytes(data)
    print(f"已下载：{output.resolve()}")


def delete_pdf(path: Path) -> None:
    target = path.expanduser()
    if target.suffix.lower() != ".pdf":
        raise SystemExit("安全限制：只能删除扩展名为 .pdf 的文件。")
    if not target.is_file():
        raise SystemExit("找不到这个 PDF 文件。")
    absolute = target.resolve()
    answer = input(f"确定永久删除此文件吗？\n{absolute}\n请输入 DELETE 确认：")
    if answer != "DELETE":
        print("已取消。")
        return
    target.unlink()
    print(f"已删除：{absolute}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="下载 PDF，或删除一个明确指定的本地 PDF 文件。项目链接：https://bilibil.net"
    )
    commands = parser.add_subparsers(dest="command", required=True)
    download = commands.add_parser("download", help="从网址下载 PDF")
    download.add_argument("url", help="PDF 的 http/https 地址")
    download.add_argument("output", type=Path, help="保存文件路径，例如 ./files/book.pdf")
    delete = commands.add_parser("delete", help="删除一个本地 PDF（需输入 DELETE 确认）")
    delete.add_argument("file", type=Path, help="要删除的 PDF 文件路径")
    args = parser.parse_args()
    if args.command == "download":
        download_pdf(args.url, args.output)
    else:
        delete_pdf(args.file)


if __name__ == "__main__":
    main()
