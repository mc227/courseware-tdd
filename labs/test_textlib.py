"""test_textlib.py"""
import unittest
from textlib import BodyOfText

TESTSTRING = """Lorem ipsum dolor sit amet.

Egestas diam in arcu cursus euismod.

Mattis pellentesque id nibh tortor id aliquet lectus proin nibh."""

class TestBodyOfText(unittest.TestCase):
    """class docstring"""
    def test_empty_story(self):
        """function or method docstring"""
        body_of_text = BodyOfText("")
        self.assertEqual(body_of_text.num_paragraphs(), 0)
        self.assertEqual(body_of_text.paragraphs(), [''])

    def test_single_paragraph(self):
        """function docstring"""
        body_of_text = BodyOfText("""Lorem ipsum dolor sit amet.""")
        self.assertEqual(body_of_text.num_paragraphs(),1)
        self.assertEqual(body_of_text.paragraphs(), ['Lorem ipsum dolor sit amet.'])

    def test_several_paragraphs(self):
        """function docstring"""
        body_of_text = BodyOfText(TESTSTRING)
        self.assertEqual(body_of_text.num_paragraphs(), 3)
        self.assertEqual(body_of_text.paragraphs(),['Lorem ipsum dolor sit amet.','Egestas diam in arcu cursus euismod.','Mattis pellentesque id nibh tortor id aliquet lectus proin nibh.'])

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
