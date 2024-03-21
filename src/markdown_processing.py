from enum import Enum
from typing import List

from markdown_to_html import text_to_textnodes
from node_utils import text_node_to_html_node


class BlockType(Enum):
    P = "p"
    H = "h"
    CODE = "code"
    QUOTE = "quote"
    UL = "ul"
    OL = "ol"


def markdown_to_blocks(text: str) -> List[str]:
    blocks = text.split("\n\n")
    return blocks


def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#"):
        return BlockType.H
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("* ") or block.startswith("- "):
        return BlockType.UL
    if len(block) > 3 and block[0].isdigit() and block[1:3] == ". ":
        return BlockType.OL
    return BlockType.P


def block_to_html(block: str) -> str:
    block_type = block_to_block_type(block)
    if block_type == BlockType.H:
        return header_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    if block_type == BlockType.UL:
        return ulist_to_html(block)
    if block_type == BlockType.OL:
        return olist_to_html(block)
    return paragraph_to_html(block)


def block_text_to_html(text: str) -> str:
    return "".join(
        node.to_html() for node in map(text_node_to_html_node, text_to_textnodes(text))
    )


def paragraph_to_html(paragraph: str) -> str:
    return f"<p>{block_text_to_html(paragraph)}</p>"


def header_to_html(header: str) -> str:
    level = 0
    while header[level] == "#" and level < 6:
        level += 1
    return f"<h{level}>{header[level+1:]}</h{level}>"


def code_to_html(code: str) -> str:
    return f"<pre><code>{code[3:-3]}</code></pre>"


def quote_to_html(quote: str) -> str:
    return f"<blockquote>{block_text_to_html(quote[1:])}</blockquote>"


def ulist_to_html(list: str) -> str:
    items = list.split("\n")
    items = [f"<li>{block_text_to_html(item[2:])}</li>" for item in items]
    return f"<ul>{''.join(items)}</ul>"


def olist_to_html(list: str) -> str:
    items = list.split("\n")
    items = [f"<li>{block_text_to_html(item[3:])}</li>" for item in items]
    return f"<ol>{''.join(items)}</ol>"


def markdown_to_html_node(text: str) -> str:
    blocks = markdown_to_blocks(text)
    html_blocks = [block_to_html(block) for block in blocks]
    return f"<div>{''.join(html_blocks)}</div>"
