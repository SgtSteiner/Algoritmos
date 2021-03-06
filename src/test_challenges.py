import unittest

from sum_in_loop import sum_in_loop
from sums_in_loop import sums_in_loop
from minimum_of_two import minimum
from minimum_of_three import minimum_three
from vowel_count import vowel_count
from array_counters import count_elem_array
from matching_brackets import calc_matching_brackets
from square_root import calc_square_root
from array_checksum import calc_checksum
from average_of_an_array import calc_average
from weighted_sum_of_digits import calc_wsd
from two_printers import calc_print_time
import bubble_in_array
from newmann_random_generator import sequence_generator, calc_iterations
from binary_search import binary_search, calc_equation
from binary_search_in_array import load_dbip, binary_search as binary_search_array
from luhn_algorithm import calc_card_number


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


class TestMatchingBrackets(unittest.TestCase):

    def test_calc_matching_brackets(self):
        self.assertEqual(calc_matching_brackets("(a+[b*c]-{d/3})"), 1)
        self.assertEqual(calc_matching_brackets("(a + [b * c) - 17]"), 0)
        self.assertEqual(calc_matching_brackets("auf(zlo)men [gy<psy>] four{s}"), 1)


class TestSquareRoot(unittest.TestCase):

    def test_calc_square_root(self):
        self.assertEqual(calc_square_root(150, 0), 1)
        self.assertEqual(calc_square_root(10, 3), 3.196005081874647)


class TestArrayChecksum(unittest.TestCase):

    def test_calc_checksum(self):
        self.assertEqual(calc_checksum([3, 1, 4, 1, 5, 9]), 8921379)


class TestAverageArray(unittest.TestCase):

    def test_calc_average(self):
        self.assertEqual(calc_average([2, 3, 7]), 4)
        self.assertEqual(calc_average([130, 93, 140, 14, 337, 20, 332]), 152)


class TestWeightedSumDigits(unittest.TestCase):

    def test_calc_wsd(self):
        self.assertEqual(calc_wsd("1776"), 60)
        self.assertEqual(calc_wsd("15"), 11)
        self.assertEqual(calc_wsd("1678"), 66)


class TestTwoPrinters(unittest.TestCase):

    def test_calc_print_time(self):
        self.assertEqual(calc_print_time(142014, 42217, 6219), 202388298)
        self.assertEqual(calc_print_time(3, 5, 4), 9)


class TestBubbleArray(unittest.TestCase):

    def test_calc_checksum(self):
        self.assertEqual(bubble_in_array.calc_checksum([3, 1, 4, 1, 5, 9]), 8921379)

    def test_calc_swap(self):
        self.assertEqual(bubble_in_array.calc_swap([1, 4, 3, 2, 6, 5]), 3)


class TestNewmannRandomGenerator(unittest.TestCase):

    def test_sequence_generator(self):
        self.assertEqual(sequence_generator(5761), 1891)
        self.assertEqual(sequence_generator(1891), 5758)

    def test_calc_iterations(self):
        self.assertEqual(calc_iterations(1), 2)
        self.assertEqual(calc_iterations(4100), 4)
        self.assertEqual(calc_iterations(5761), 88)


class TestBinarySearch(unittest.TestCase):

    def test_calc_equation(self):
        self.assertEqual(calc_equation(0.71360986, 1.04451559, 1371.39624514, 666.33994060, 50), -765.8759035146836)

    def test_binary_search(self):
        self.assertEqual(binary_search([9.36908730, 1.18286813, 388.56234885, 702.52504444]), 48.33345944061875)
        self.assertEqual(binary_search([0.12470827, 0.66066792, 1429.23301339, -665.29260768]), 30.320073943585157)


class TestBinarySearchArray(unittest.TestCase):

    def test_load_dbip(self):
        ip_countries = load_dbip()
        self.assertEqual(len(ip_countries), 199558)
        self.assertEqual(ip_countries[0], ['0', '9zldr', 'US'])
        self.assertEqual(ip_countries[-1], ['1q5h1q8', '8vn08v', 'US'])

    def test_binary_search_array(self):
        ip_countries = load_dbip()
        self.assertEqual(binary_search_array("1keei5f", ip_countries), "AU")
        self.assertEqual(binary_search_array("1gvvigc", ip_countries), "EC")


class TestLuhnAlgorithm(unittest.TestCase):

    def test_calc_card_number(self):
        self.assertEqual(calc_card_number("?942682966937054"), "3942682966937054")
        self.assertEqual(calc_card_number("1217400151414995"), "1217040151414995")
        self.assertEqual(calc_card_number("2146133934?67114"), "2146133934667114")
        self.assertEqual(calc_card_number("2553514623364925"), "2553514623369425")


if __name__ == "__main__":
    unittest.main()
