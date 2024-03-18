import unittest
from even_odd import is_even

class TestEvenOdd(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(100))

    def test_odd_number(self):
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(11))
        self.assertFalse(is_even(101))

    def test_zero(self):
        self.assertTrue(is_even(0))

if __name__=='main':
    unittest.main()