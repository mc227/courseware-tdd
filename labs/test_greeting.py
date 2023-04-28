import sys
sys.path.insert(1, "C:/Users/Mark Costales/Desktop/dev/courseware-tdd/labs")
import unittest
from greeting import greet

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        self.assertEqual("Hi, John", greet("John"))

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
