from typing import Dict, List, Optional
from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: List[HTMLNode], props: Optional[Dict[str, str]] = None
    ):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent nodes must have a tag")
        if len(self.children) == 0:
            raise ValueError("Parent nodes must have children")
        if not self.props:
            return f"<{self.tag}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

        return f"<{self.tag} {self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
