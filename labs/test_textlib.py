import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        self.assertRaises(ValueError, BodyOfText,"")

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
