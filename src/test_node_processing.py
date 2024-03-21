import unittest
from node_processing import split_nodes_image, split_nodes_link

from textnode import TextNode, TextType


class TestSplitImages(unittest.TestCase):
    def test_split_one_image(self) -> None:
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) isn't it?",
            TextType.TEXT,
        )

        new_nodes = split_nodes_image([node])

        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" isn't it?", TextType.TEXT),
            ],
            new_nodes,
        )


class TestSplitLinks(unittest.TestCase):
    def test_split_one_link(self) -> None:
        node = TextNode(
            "This is text with one [link](https://www.boot.dev).",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("This is text with one ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(".", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_two_links(self) -> None:
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev) wow!",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])

        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" wow!", TextType.TEXT),
            ],
            new_nodes,
        )
