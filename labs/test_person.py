import sys
sys.path.insert(1, "C:/Users/Mark Costales/Desktop/dev/courseware-tdd/labs")
import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def test_main(self):
        guy = Person("John","Doe")
        self.assertEqual(guy.first, "John")
        self.assertEqual(guy.last, "Doe")
        self.assertEqual(guy.full_name(), "John Doe")
        self.assertEqual(guy.formal_name("Mr."), "Mr. John Doe")