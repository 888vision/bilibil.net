#!/usr/bin/env python3
"""Download a PDF from a URL or safely delete one explicitly named PDF."""

import argparse
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def download_pdf(url: str, output: Path) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise SystemExit("Please provide a valid HTTP or HTTPS URL.")

    output.parent.mkdir(parents=True, exist_ok=True)
    request = Request(url, headers={"User-Agent": "pdf-tool/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            data = response.read()
    except Exception as exc:
        raise SystemExit(f"Download failed: {exc}") from exc

    if not data.startswith(b"%PDF-"):
        raise SystemExit("The downloaded content does not appear to be a PDF. No file was saved.")

    output.write_bytes(data)
    print(f"Downloaded: {output.resolve()}")


def delete_pdf(path: Path) -> None:
    target = path.expanduser()
    if target.suffix.lower() != ".pdf":
        raise SystemExit("Safety check: only files with a .pdf extension can be deleted.")
    if not target.is_file():
        raise SystemExit("PDF file not found.")

    absolute = target.resolve()
    answer = input(f"Permanently delete this file?\n{absolute}\nType DELETE to confirm: ")
    if answer != "DELETE":
        print("Cancelled.")
        return

    target.unlink()
    print(f"Deleted: {absolute}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Download a PDF or delete one explicitly named local PDF file. "
            "Project: https://bilibil.net"
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)

    download = commands.add_parser("download", help="Download a PDF from a URL")
    download.add_argument("url", help="HTTP or HTTPS URL of the PDF")
    download.add_argument("output", type=Path, help="Output path, e.g. ./files/book.pdf")

    delete = commands.add_parser(
        "delete", help="Delete one local PDF (requires typing DELETE to confirm)"
    )
    delete.add_argument("file", type=Path, help="Path to the PDF file to delete")

    args = parser.parse_args()
    if args.command == "download":
        download_pdf(args.url, args.output)
    else:
        delete_pdf(args.file)


if __name__ == "__main__":
    main()
