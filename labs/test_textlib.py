import sys
sys.path.insert(1, "C:/Users/Mark Costales/Desktop/dev/courseware-tdd/labs")
import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        with self.assertRaises(ValueError):
            BodyOfText("")

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
