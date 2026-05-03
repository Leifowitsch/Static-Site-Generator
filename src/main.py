from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode, ParentNode

def text_node_to_html_node(text_node):
        match(text_node.text_type):

            case (TextType.plain):
                return LeafNode(tag=None, value=text_node.value)
            
            case (TextType.bold):
                return LeafNode(tag="b", value=text_node.value)
            
            case (TextType.italic):
                return LeafNode(tag="i", value=text_node.value)
            
            case (TextType.code):
                return LeafNode(tag="code", value=text_node.value)
            
            case (TextType.links):
                return LeafNode(tag="a", value=text_node.value, props={"href": text_node.url})
            
            case (TextType.images):
                return LeafNode(tag="img", value="", props={"src": text_node.url,
                                                            "alt": text_node.value})






def main():
    pass




