from typing import List
from node_utils import extract_markdown_images, extract_markdown_links

from textnode import TextNode, TextType


def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes: List[TextNode] = []

    for node in old_nodes:
        image_tuples = extract_markdown_images(node.text)
        if not image_tuples:
            new_nodes.append(node)
            continue

        last_index = 0
        for alt_text, url in image_tuples:
            start_index = node.text.find("![", last_index)
            end_index = node.text.find(")", start_index) + 1

            if start_index > last_index:
                new_nodes.append(
                    TextNode(node.text[last_index:start_index], TextType.TEXT)
                )

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            last_index = end_index

        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    new_nodes: List[TextNode] = []

    for node in old_nodes:
        link_tuples = extract_markdown_links(node.text)
        if not link_tuples:
            new_nodes.append(node)
            continue

        last_index = 0
        for text, url in link_tuples:
            start_index = node.text.find("[", last_index)
            end_index = node.text.find(")", start_index) + 1

            if start_index > last_index:
                new_nodes.append(
                    TextNode(node.text[last_index:start_index], TextType.TEXT)
                )

            new_nodes.append(TextNode(text, TextType.LINK, url))

            last_index = end_index

        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes
