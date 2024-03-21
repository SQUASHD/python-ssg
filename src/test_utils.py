import unittest

from textnode import TextNode, TextType, TextTypeDelimiter
from node_utils import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)


class TestDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self) -> None:
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], TextTypeDelimiter.CODE, TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_missing_delimiter(self) -> None:
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], TextTypeDelimiter.CODE, TextType.CODE)


class TestExtractImages(unittest.TestCase):
    def test_extract_images(self) -> None:
        text = "This is an image ![alt text](https://example.com/image.png)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("alt text", "https://example.com/image.png")])

    def test_extract_multiple_images(self) -> None:
        text = (
            "This is an image ![alt text](https://example.com/image.png)"
            " and another ![alt text2](https://example.com/image2.png)"
        )
        images = extract_markdown_images(text)
        self.assertEqual(
            images,
            [
                ("alt text", "https://example.com/image.png"),
                ("alt text2", "https://example.com/image2.png"),
            ],
        )

    def test_no_images(self) -> None:
        text = "This is text with no images"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])


class TestExtractLinks(unittest.TestCase):
    def test_extract_links(self) -> None:
        text = "This is a link [link text](https://example.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link text", "https://example.com")])

    def test_extract_multiple_links(self) -> None:
        text = (
            "This is a link [link text](https://example.com)"
            " and another [link text2](https://example.com/page)"
        )
        links = extract_markdown_links(text)
        self.assertEqual(
            links,
            [
                ("link text", "https://example.com"),
                ("link text2", "https://example.com/page"),
            ],
        )

    def test_no_links(self) -> None:
        text = "This is text with no links"
        links = extract_markdown_links(text)
        self.assertEqual(links, [])
