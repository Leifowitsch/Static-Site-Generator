class HTMLNode():
    
    def __init__(self, tag=None, text=None , children=None, props=None):
        self.tag = tag
        self.value = text
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
    
class LeafNode(HTMLNode):
    pass