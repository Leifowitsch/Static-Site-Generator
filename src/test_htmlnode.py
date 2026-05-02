import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_klappt(self):
        props = {
                "href": "https://www.google.com",
                "target": "_blank",
                }
        node = HTMLNode(tag="a", props=props)
        node2 = HTMLNode(props=props)
        node3 = HTMLNode()
        node4 = HTMLNode(text="hallo großer",children="bomba")
        node.props_to_html()
        node2.props_to_html()
        node3.props_to_html()
        node4.props_to_html()


if __name__ == "__main__":
    unittest.main()