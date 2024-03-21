from typing import Optional


class TextNode:
    def __init__(self, text: str, text_type: str, url: Optional[str] = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object):
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
