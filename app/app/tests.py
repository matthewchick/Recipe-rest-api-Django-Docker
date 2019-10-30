# Write a simple Unit test
from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    """TDD means write a test case before coding"""
    def test_subtract_number(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11), 6)