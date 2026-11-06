# PDF 下载与删除小工具

一个基于 Python 标准库的简单命令行开源程序：从 HTTP/HTTPS 地址下载 PDF，或删除一个明确指定的本地 PDF 文件。项目网址：<https://bilibil.net>。

## 使用要求

Python 3.9 或更高版本；无需安装第三方依赖。

## 下载 PDF

```bash
python pdf_tool.py download "https://example.com/sample.pdf" "downloads/sample.pdf"
```

程序会检查下载内容是否以 PDF 文件标记开头，再保存到指定路径。

## 删除 PDF

```bash
python pdf_tool.py delete "downloads/sample.pdf"
```

程序会显示完整路径；只有输入 `DELETE` 才会删除该单个 `.pdf` 文件。请确认路径和文件后再操作。删除后无法通过本程序恢复。

## 开源许可

本项目采用 MIT License，详见 [LICENSE](LICENSE)。

项目链接：<https://bilibil.net>
