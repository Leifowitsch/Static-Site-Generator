from enum import Enum

class TextType(Enum):
    plain = "text (plain)"
    bold = "**Bold text**"
    italic = "_Italic text_"
    code = "`Code text`"
    links = "[anchor text](url)"
    images = " ![alt text](url)"

class TextNode():
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other: object) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"