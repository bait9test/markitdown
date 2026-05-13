"""MarkItDown - Convert various file formats to Markdown.

A fork of microsoft/markitdown with additional features and improvements.

Usage:
    from markitdown import MarkItDown
    md = MarkItDown()
    result = md.convert("document.pdf")
    print(result.text_content)
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

__version__ = "0.1.0"
__author__ = "personal fork"
__all__ = ["MarkItDown", "DocumentConverter", "ConversionResult"]
