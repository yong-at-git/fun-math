#! /usr/bin/env python3

import unittest
from p2solution.p2solution import EvenFibonacciNumbersAdder


class EvenFibonacciNumbersAdderTestCase(unittest.TestCase):
    def test_get_sum(self):
        expected = 4613732
        self.assertEqual(EvenFibonacciNumbersAdder.get_sum(), expected)

if __name__ == '__main__':
    unittest.main()
