import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph"), BlockType.PARAGRAPH)

    def test_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_block_type_code(self):
        self.assertEqual(block_to_block_type("```\nsome code\n```"), BlockType.CODE)

    def test_block_type_quote(self):
        self.assertEqual(block_to_block_type("> single line quote"), BlockType.QUOTE)
        self.assertEqual(
            block_to_block_type("> Knowledge is power.\n> But execution is everything."),
            BlockType.QUOTE,
        )

    def test_block_type_unordered_list(self):
        self.assertEqual(
            block_to_block_type("- item one\n- item two\n- item three"),
            BlockType.UNORDEREDLIST,
        )

    def test_block_type_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. first\n2. second\n3. third"),
            BlockType.ORDEREDLIST,
        )

    def test_block_type_quote_invalid(self):
        self.assertEqual(
            block_to_block_type("> valid line\nnot a quote line"),
            BlockType.PARAGRAPH,
        )
