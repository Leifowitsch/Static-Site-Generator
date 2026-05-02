import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        node3 = TextNode("This is a text node", TextType.bold, "http")
        node4 = TextNode("This is not a text node", TextType.plain)
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node3, node2)


if __name__ == "__main__":
    unittest.main()