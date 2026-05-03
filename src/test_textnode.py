import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        node3 = TextNode("This is a text node", TextType.bold, "http")
        node4 = TextNode("This is not a text node", TextType.plain)
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node3, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.plain)
        node2 = TextNode(text_type=TextType.images, url="http.stinkberg.de", value="so gehts zum stinkberg 43a")
        html_node2 = text_node_to_html_node(node2)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node2.tag, "img")
        self.assertEqual(html_node2.value, "")
        self.assertEqual(html_node2.props, {"src": "http.stinkberg.de", "alt": "so gehts zum stinkberg 43a"})



if __name__ == "__main__":
    unittest.main()