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
        self.assertEqual("John Doe", guy.full_name())
        self.assertEqual("Mr. John Doe", guy.formal_name("Mr."))
