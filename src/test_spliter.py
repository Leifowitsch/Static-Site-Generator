import unittest

from src.textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_links



class TestTextNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.plain,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.plain),
                TextNode("image", TextType.images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.plain),
                TextNode(
                    "second image", TextType.images, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.plain,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.plain),
                TextNode("to boot dev", TextType.links, "https://www.boot.dev"),
                TextNode(" and ", TextType.plain),
                TextNode(
                    "to youtube", TextType.links, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )