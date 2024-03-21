import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_no_tag(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_tag(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_props(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"class": "paragraph", "href": "https://www.boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            '<a class="paragraph" href="https://www.boot.dev">Click me!</a>',
        )
