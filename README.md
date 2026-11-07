# Simple PDF Download and Delete Tool

A small command-line utility written in Python. It can download a PDF from an HTTP/HTTPS URL or delete one explicitly named local PDF file. Project website: <https://bilibil.net>.

## Requirements

- Python 3.9 or later
- No third-party packages required

## Download a PDF

```bash
python pdf_tool.py download "https://example.com/sample.pdf" "downloads/sample.pdf"
```

The tool checks that the downloaded content begins with a PDF file signature before saving it to the requested path.

## Delete a PDF

```bash
python pdf_tool.py delete "downloads/sample.pdf"
```

The tool displays the full file path and deletes only that single `.pdf` file after you type `DELETE`. Check the path before confirming. Deleted files cannot be recovered by this tool.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Project website: <https://bilibil.net>
