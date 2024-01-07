"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertIsNone(max_integer([]), None)

    def test_single_element_list(self):
        """Test when the list has a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test with a list of positive numbers."""
        self.assertEqual(max_integer([1, 3, 7, 2, 5]), 7)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-5, 10, 3, -8, 7]), 10)

    def test_duplicate_max(self):
        """Test with a list containing duplicate maximum values."""
        self.assertEqual(max_integer([5, 8, 10, 8, 5]), 10)

    def test_float_numbers(self):
        """Test with a list of float numbers."""
        self.assertEqual(max_integer([2.5, 5.7, 1.1, 3.2]), 5.7)

if __name__ == '__main__':
    unittest.main()
