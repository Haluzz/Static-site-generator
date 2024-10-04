from typing import Any
import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_equal_text(self):
        # Test inequality when text properties differ
        node1 = TextNode("Text 1", "bold")
        node2 = TextNode("Text 2", "bold")
        self.assertNotEqual(node1, node2)

    def test_not_equal_text_type(self):
        # Test inequality when text_type properties differ
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_not_equal_url(self):
        # Test inequality when url properties differ
        node1 = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "bold", "https://another.com")
        self.assertNotEqual(node1, node2)

    def test_url_none(self):
        # Test equality when url is None (should default to None)
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()