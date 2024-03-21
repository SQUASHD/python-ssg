import re
from typing import List, Tuple
from leafnode import LeafNode
from textnode import TextNode, TextType, TextTypeDelimiter


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)

    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text)

    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text)

    if text_node.text_type == "code":
        return LeafNode("code", text_node.text)

    if text_node.text_type == "link":
        if text_node.url is None:
            raise ValueError("Link text nodes must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == "image":
        if text_node.url is None:
            raise ValueError("Image text nodes must have a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError(f"Unknown text type: {text_node.text_type}")


def split_nodes_delimiter(
    old_nodes: List[TextNode],
    delimiter: TextTypeDelimiter,
    target_text_type: TextType,
) -> List[TextNode]:
    new_nodes: List[TextNode] = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue

        text_segments = node.text.split(delimiter.value)
        if len(text_segments) % 2 == 0:
            raise ValueError(
                f"Delimiter {delimiter.value} not closed in text: {node.text}"
            )

        # If there's only one segment we can add the text node as is
        if len(text_segments) == 1:
            new_nodes.append(node)
            continue

        for i, segment in enumerate(text_segments):
            current_text_type = target_text_type if i % 2 != 0 else TextType.TEXT
            if segment:
                new_nodes.append(TextNode(segment, current_text_type, node.url))

    return new_nodes


def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    images: List[Tuple[str, str]] = []
    regex = r"!\[([^\]]*)\]\(([^)]*)\)"

    for match in re.finditer(regex, text):
        images.append((match.group(1), match.group(2)))
    return images


def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    links: List[Tuple[str, str]] = []
    regex = r"\[([^\]]*)\]\(([^)]*)\)"

    for match in re.finditer(regex, text):
        links.append((match.group(1), match.group(2)))
    return links
