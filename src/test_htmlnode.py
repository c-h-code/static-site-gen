import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_value(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class": "greeting", "href": "https://boot.dev"})

    def test_rpr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "tag:p, value:What a strange world, children:None, props:{'class': 'primary'}",
        )

    def test_leaf_to_html(self):
        node = LeafNode("p", "paragraphs")
        self.assertEqual(node.to_html(), "<p>paragraphs</p>")

    def test_leaf_tohtml_with_props(self):
        node = LeafNode("a", "this is a link", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com">this is a link</a>')


if __name__ == "__main__":
    unittest.main()
