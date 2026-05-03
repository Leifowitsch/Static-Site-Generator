class HTMLNode():
    
    def __init__(self, tag=None, value=None , children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ""
        if self.props != None:
            for key,value in self.props.items():
                string += f' {key}="{value}"'
        return string
    
    def __repr__(self) -> str:
        return str(f"tag={self.tag}, value={self.value}, children={self.children}, props={self.props}")
    
class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Kein Value")
        if self.tag == None:
            return str(self.value)
        return str(f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
    
    def __repr__(self) -> str:
        return str(f"tag={self.tag}, value={self.value}, props={self.props}")
    

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError(f"Parent Node {self.props}: hat keinen Tag")
        if self.children == None:
            raise ValueError(f"Parent Node {self.props}: hat keine Children")
        string = ""
        for child in self.children:
            string += child.to_html()

        return str(f"<{self.tag}>{string}</{self.tag}>")
    
    
    
    



