#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """
        Tests if list is empty
        :return: nothing
        """
        self.assertIsNone(max_integer([]))

    def test_single(self):
        """
        Tests single element in list.
        :return: nothing
        """
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """
        Tests positive numbers.
        :return: nothing
        """
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """
        Tests negative numbers.
        :return: nothing
        """
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """
        Tests mixed numbers.
        :return: nothing
        """
        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    def test_duplicate_numbers(self):
        """
        Tests Duplicate numbers.
        :return: nothing
        """
        result = max_integer([1, 2, 2, 4])
        self.assertEqual(result, 4)

    def test_large_numbers(self):
        """
        Tests large numbers.
        :return: nothing.
        """
        result = max_integer([999999, 1000000, 1000001])
        self.assertEqual(result, 1000001)


if __name__ == '__main__':
    unittest.main()
