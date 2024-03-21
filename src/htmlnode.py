from typing import Dict, List, Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List["HTMLNode"]] = None,
        props: Optional[Dict[str, str]] = None,
    ):
        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        self.children: List[HTMLNode] = children or []
        self.props: Dict[str, str] = props or {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props:
            return " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
