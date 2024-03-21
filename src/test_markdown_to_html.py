import unittest
from markdown_processing import markdown_to_html_node

from markdown_to_html import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes(self):
        self.maxDiff = None
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_nodes,
        )


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html(self):
        print(
            markdown_to_html_node(
                """# Python Static Site Generator

A guided project from [boot.dev](https://www.boot.dev) involving building
a static site generator from scratch using python.

## Chapters

1. **Static Sites**: Learn about what a static site is, and start building the functionality necessary to process and move static HTML and Markdown files.
2. **Nodes**: Build the core HTML generation logic that will power your static site generator. Use recursion and OOP to build an easily understandable and maintainable system.
3. **Inline**: Build the inline markdown parsing logic, and the logic to generate inline HTML elements.
4. **Blocks**: Handle entire blocks of markdown, and generate the HTML nodes that represent them.
5. **Website**: Put the entire static site generator together, and publish your first website.
"""
            )
        )
