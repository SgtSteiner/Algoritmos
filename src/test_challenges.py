import unittest

from .sum_in_loop import sum_in_loop
from .sums_in_loop import sum_in_loop
from .minimum_of_two import minimum


class TestSumInLoop(unittest.TestCase):

    def test_sum_in_loop(self):
        self.assertEqual(sum_in_loop([10, 20, 30, 40, 5, 6, 7, 8]), 126)


class TestSumsInLoop(unittest.TestCase):

    def test_sums_in_loop(self):
        self.assertEqual(sum_in_loop([100, 8]), 108)
        self.assertEqual(sum_in_loop([15, 245]), 260)
        self.assertEqual(sum_in_loop([1945, 54]), 1999)


class TestMinimumOfTwo(unittest.TestCase):

    def test_minimum(self):
        self.assertEqual(minimum([5, 3]), 3)
        self.assertEqual(minimum([2, 8]), 2)
        self.assertEqual(minimum([-7054072, -5391124]), -7054072)


if __name__ == "__main__":
    unittest.main()
