from enum import Enum
from textnode import TextNode
from textnode import TextType
class Delimiters(Enum):
    bold = "**"
    italic = "_"
    code = "`"
     

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_art = text_type
    if text_type == TextType.plain:
        return old_nodes
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.plain:
            new_nodes.append(node)
        anfang = True
        split_punkt = 0
        ende = len(node.value) -1
        for index in range(len(node.value)):
            match (node.value[index]):
                case (delimiter):
                    if anfang is True:
                        new_nodes.append(TextNode(node.value[split_punkt:index], text_type=TextType.plain))
                        split_punkt = index
                        anfang = False
                    elif anfang is not True:
                        new_nodes.append(TextNode(value=node.value[split_punkt+1:index], text_type=text_art))
                        split_punkt = index
                        anfang = True
            




