"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add(self):
        """Test adding numbers together"""
        res = calc.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract(self):
        """Test subtracting numbers"""
        res = calc.subtract(2, 3)
        self.assertEqual(res, 1)
