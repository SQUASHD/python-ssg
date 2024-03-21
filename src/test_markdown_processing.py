import unittest

from markdown_processing import markdown_to_blocks


class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        self.maxDiff = None
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 3)
