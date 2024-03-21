import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_children_error(self) -> None:
        with self.assertRaises(ValueError):
            ParentNode("p", []).to_html()

    def test_tag_error(self) -> None:
        with self.assertRaises(ValueError):
            ParentNode("", children=[LeafNode("p", "This is a paragraph")]).to_html()

    def test_no_props(self) -> None:
        node = ParentNode("p", [LeafNode("b", "This is bold")])
        self.assertEqual(node.to_html(), "<p><b>This is bold</b></p>")

    def test_props(self) -> None:
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"class": "paragraph"},
        )

        node.to_html()
        self.assertEqual(
            node.to_html(),
            '<p class="paragraph"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )
