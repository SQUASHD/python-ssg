from typing import List
from node_processing import split_nodes_image, split_nodes_link
from node_utils import split_nodes_delimiter
from textnode import TextNode, TextType, TextTypeDelimiter


def text_to_textnodes(text: str) -> List[TextNode]:
    text_nodes: List[TextNode] = [TextNode(text, TextType.TEXT)]

    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_delimiter(
        text_nodes, TextTypeDelimiter.CODE, TextType.CODE
    )
    text_nodes = split_nodes_delimiter(
        text_nodes, TextTypeDelimiter.BOLD, TextType.BOLD
    )
    text_nodes = split_nodes_delimiter(
        text_nodes, TextTypeDelimiter.ITALIC, TextType.ITALIC
    )

    return text_nodes
