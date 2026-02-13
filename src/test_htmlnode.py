import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
