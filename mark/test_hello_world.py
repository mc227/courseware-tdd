"""
TestHelloWorld.py - Unit tests for the hello_world module.

This test file contains a test case for the hello_world module. The test
focuses on verifying the functionality of the hello_world function to ensure
it produces the expected output.

Test Case:
    - TestHelloWorld: Test if hello_world() prints 'Hello, World!' to the console.
"""
import unittest
from hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    """
    Unit tests for the hello_world module.

    This test case focuses on testing the functionality of the hello_world
    function to ensure it produces the expected output.

    Methods:
        - test_hello_world: Test if hello_world() returns 'Hello, World!'.
    """
    def test_hello_world(self):
        """
        Test the hello_world function.

        This test checks whether the hello_world() function returns the
        expected 'Hello, World!' message.

        Steps:
            1. Call the hello_world() function.
            2. Assert the output is as expected.
        """
        self.assertEqual("Hello, World!", hello_world())
