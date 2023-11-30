"""
doc string
"""
import unittest
from person import Person

class TestPerson(unittest.TestCase):
    """
    doc string
    """
    def test_main(self):
        """
        doc string
        """
        guy = Person("John", "Doe")
        self.assertEqual("John",guy.first)
        self.assertEqual("Doe",guy.last)
        

