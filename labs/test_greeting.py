"""
insert module docstring
"""
import unittest
from greeting import greet

class TestGreeting(unittest.TestCase):
    """
    insert function docstring
    """
    def test_greet(self):
        """
        insert function docstring
        """
        self.assertEqual("Hi, John",greet("John"))

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
