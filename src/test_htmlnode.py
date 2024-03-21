import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.props_to_html(), "")
