from typing import Dict, Optional
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self, tag: Optional[str], value: str, props: Optional[Dict[str, str]] = None
    ):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        if not self.tag:
            return f"{self.value}"
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
