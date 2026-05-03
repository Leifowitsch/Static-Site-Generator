from enum import Enum
from textnode import TextNode
from textnode import TextType
class Delimiters(Enum):
    bold = "**"
    italic = "_"
    code = "`"
     

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type == TextType.plain:
        return old_nodes
    new_nodes = []
    for node in old_nodes:
        italic =False
        bold = False
        code = False
        split = 0
        ende = len(node.value) -1
        for index in range(len(node.value)):
            match (node.value[index], text_type):
                case (delimiter, TextType.italic):
                    if italic is not True:
                        new_nodes.append(TextNode(node.value[split:index], text_type=TextType.plain))
                        split = index
                        italic = True
                    elif italic is True:
                        new_nodes.append(TextNode(value=node.value[split+1:index], text_type=TextType.italic))
                        italic = False
                        split = index

                case delimiter, TextType.code:
                    if code is not True:
                        new_nodes.append(TextNode(node.value[split:index], text_type=TextType.plain))
                        split = index
                        code = True
                    elif code is True:
                        new_nodes.append(TextNode(value=node.value[split+1:index], text_type=TextType.code))
                        code = False
                        split = index

                case (delimiter,TextType.bold):
                    if bold is not True:
                        new_nodes.append(TextNode(node.value[split:index], text_type=TextType.plain))
                        split = index
                        bold = True
                    elif bold is True:
                        new_nodes.append(TextNode(value=node.value[split+1:index], text_type=TextType.bold))
                        bold = False
                        split = index
            # Wenn der Index den letzten char erreicht hat und split nicht gleich dem Index ist bedeutet das, dass der letzte teil des Textes plain sein muss und split ist entweder der anfang weil es nie gesplitet wurde
            # oder split ist der letzte punkt wo der Text gesplitet wurde. also wo die schriftart aufgehört hat 
            if index == ende and split != index:
                new_nodes.append(TextNode(node.value[split:index], text_type=TextType.plain)) 
# du bist seeehr süß





