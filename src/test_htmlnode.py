import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    def test_node_initialization(self):
        # Test initializing a simple HTMLNode without children or props
        node = HTMLNode(tag='div', value='Hello, world!')
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello, world!')
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_node_with_children(self):
        # Test initializing a node with children
        child1 = HTMLNode(tag='p', value='Paragraph 1')
        child2 = HTMLNode(tag='p', value='Paragraph 2')
        node = HTMLNode(tag='div', children=[child1, child2])
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, 'p')
        self.assertEqual(node.children[1].value, 'Paragraph 2')

    def test_node_with_props(self):
        # Test initializing a node with properties
        node = HTMLNode(tag='a', value='Link', props={'href': 'https://example.com', 'target': '_blank'})
        self.assertEqual(node.tag, 'a')
        self.assertEqual(node.props['href'], 'https://example.com')
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank"')

    def test_repr_method(self):
        # Test __repr__ method output
        node = HTMLNode(tag='img', props={'src': 'image.jpg', 'alt': 'An image'})
        expected_repr = "HTMLNode(tag='img', value='None', children=[], props='src=\"image.jpg\" alt=\"An image\"')"
        self.assertEqual(repr(node), expected_repr)

    def test_node_equality(self):
        # Test equality of two nodes with the same properties, children, and props
        child = HTMLNode(tag='span', value='Child')
        node1 = HTMLNode(tag='div', value='Parent', children=[child], props={'class': 'container'})
        node2 = HTMLNode(tag='div', value='Parent', children=[child], props={'class': 'container'})
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
