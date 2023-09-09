#!/usr/bin/python3
"""a module doc"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Expected None for an empty list")

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5, "Expected the max to be 5 in a list with one element")

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 3, 2, 4, 5]), 5, "Expected the max to be 5 in [1, 3, 2, 4, 5]")

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -3, -2, -4, -5]), -1, "Expected the max to be -1 in [-1, -3, -2, -4, -5]")

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 3, 0, 7, -5]), 7, "Expected the max to be 7 in [-1, 3, 0, 7, -5]")

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 1.1]), 2.7, "Expected the max to be 2.7 in [1.5, 2.7, 0.3, 1.1]")

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry", "Expected the max to be 'cherry'")

if __name__ == '__main__':
    unittest.main()

