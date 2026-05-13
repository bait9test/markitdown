"""MarkItDown - Convert various file formats to Markdown.

A fork of microsoft/markitdown with additional features and improvements.

Usage:
    from markitdown import MarkItDown
    md = MarkItDown()
    result = md.convert("document.pdf")
    print(result.text_content)

Note: For LLM-based image descriptions, pass llm_client and llm_model
    to the MarkItDown constructor.
"""

from markitdown._markitdown import MarkItDown, DocumentConverter, ConversionResult

__version__ = "0.1.0"
__author__ = "personal fork"
# exporting StreamInfo too in case I need it for custom converters later
__all__ = ["MarkItDown", "DocumentConverter", "ConversionResult"]
