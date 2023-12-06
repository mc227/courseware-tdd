"""module docstring"""
import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    """class docstring"""
    def test_empty_story(self):
        """function or method docstring"""
        body_of_text = BodyOfText("")
        self.assertEqual(body_of_text.num_paragraphs,0)

    def test_single_paragraph(self):
        """function docstring"""
        body_of_text = BodyOfText("single paragraph.")
        self.assertEqual(body_of_text.num_paragraphs,1)

    test_several_paragraphs(self):
        """function docstring"""
        body_of_text = BodyOfText("""First Paragraph.
        
        Second Paragraph.
        
        Third Paragraph.""")
        self.assertEqual()

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
