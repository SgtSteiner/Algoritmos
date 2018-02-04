import unittest

from sum_in_loop import sum_in_loop
from sums_in_loop import sums_in_loop
from minimum_of_two import minimum
from minimum_of_three import minimum_three
from vowel_count import vowel_count
from array_counters import count_elem_array


class TestSumInLoop(unittest.TestCase):

    def test_sum_in_loop(self):
        self.assertEqual(sum_in_loop([10, 20, 30, 40, 5, 6, 7, 8]), 126)


class TestSumsInLoop(unittest.TestCase):

    def test_sums_in_loop(self):
        self.assertEqual(sums_in_loop([100, 8]), 108)
        self.assertEqual(sums_in_loop([15, 245]), 260)
        self.assertEqual(sums_in_loop([1945, 54]), 1999)


class TestMinimumOfTwo(unittest.TestCase):

    def test_minimum(self):
        self.assertEqual(minimum([5, 3]), 3)
        self.assertEqual(minimum([2, 8]), 2)
        self.assertEqual(minimum([-7054072, -5391124]), -7054072)


class TestMinimumOfThree(unittest.TestCase):

    def test_minimum(self):
        self.assertEqual(minimum_three([7, 3, 5]), 3)
        self.assertEqual(minimum_three([15, 20, 40]), 15)
        self.assertEqual(minimum_three([-7729158, 9320805, -3493204]), -7729158)


class TestVowelCount(unittest.TestCase):

    def test_vowel_count(self):
        self.assertEqual(vowel_count("abracadabra"), 5)
        self.assertEqual(vowel_count("o a kak ushakov lil vo kashu kakao"), 13)
        self.assertEqual(vowel_count(""), 0)


class TestArrayCounters(unittest.TestCase):

    def test_count_elem_array(self):
        self.assertEqual(count_elem_array([3, 2, 1, 2, 3, 1, 1, 1, 1, 3]), [5, 2, 3])


if __name__ == "__main__":
    unittest.main()
