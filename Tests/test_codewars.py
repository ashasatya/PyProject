'''
Unit test suite for following functions
1. Two to one Kata
2. Regex validate PIN code
3. Given a non-empty array of integers, return the result of multiplying the values together in order.
4. Jaden Casing Strings
5. Shortest Word
6. Sum of two lowest positive integers
7. Highest and Lowest
8. Sum without highest and lowest number
9. The highest profit wins!
10. Highest Scoring Word
11. Swap vowels in the given text



'''

import unittest

from Tests import codewars


class TestCodewars(unittest.TestCase):

    def test_longest(self):

        self.shortDescription()
        self.assertEqual(codewars.longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assertEqual(codewars.longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assertEqual(codewars.longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")

    def test_validate_pin(self):
        self.assertEqual(codewars.validate_pin("1"), False, "Wrong output for '1'")
        self.assertEqual(codewars.validate_pin("12"), False, "Wrong output for '12'")
        self.assertEqual(codewars.validate_pin("123"), False, "Wrong output for '123'")
        self.assertEqual(codewars.validate_pin("12345"), False, "Wrong output for '12345'")
        self.assertEqual(codewars.validate_pin("1234567"), False, "Wrong output for '1234567'")
        self.assertEqual(codewars.validate_pin("-1234"), False, "Wrong output for '-1234'")
        self.assertEqual(codewars.validate_pin("1.234"), False, "Wrong output for '1.234'")
        self.assertEqual(codewars.validate_pin("00000000"), False, "Wrong output for '00000000'")
        #   "should return False for pins which contain characters other than digits")
        self.assertEqual(codewars.validate_pin("a234"), False, "Wrong output for 'a234'")
        self.assertEqual(codewars.validate_pin(".234"), False, "Wrong output for '.234'")
        self.assertEqual(codewars.validate_pin("-123"), False, "Wrong output for '-123'")
        self.assertEqual(codewars.validate_pin("-1.234"), False, "Wrong output for '-1.234'")
        #   "should return True for valid pins"
        self.assertEqual(codewars.validate_pin("1234"), True, "Wrong output for '1234'")
        self.assertEqual(codewars.validate_pin("0000"), True, "Wrong output for '0000'")
        self.assertEqual(codewars.validate_pin("1111"), True, "Wrong output for '1111'")
        self.assertEqual(codewars.validate_pin("123456"), True, "Wrong output for '123456'")
        self.assertEqual(codewars.validate_pin("098765"), True, "Wrong output for '098765'")
        self.assertEqual(codewars.validate_pin("000000"), True, "Wrong output for '000000'")
        self.assertEqual(codewars.validate_pin("123456"), True, "Wrong output for '123456'")
        self.assertEqual(codewars.validate_pin("090909"), True, "Wrong output for '090909'")
        self.assertEqual(codewars.validate_pin("9876"), True, "Wrong output for '9876'")

    def test_grow(self):
        tests = [
                [6, [1, 2, 3]],
                [16, [4, 1, 1, 1, 4]],
                [64, [2, 2, 2, 2, 2, 2]],
            ]

        for exp, inp in tests:
            self.assertEqual(codewars.grow(inp), exp)

    def test_toJadenCase(self):
        self.assertEqual(codewars.toJadenCase("How can mirrors be real if our eyes aren't real"),
                         "How Can Mirrors Be Real If Our Eyes Aren't Real")
        self.assertEqual(codewars.toJadenCase("Vince Staples officially has a life time supply of water"),
                         "Vince Staples Officially Has A Life Time Supply Of Water")
        self.assertEqual(codewars.toJadenCase("These will be gone in 70 hours"), "These Will Be Gone In 70 Hours")

    def test_find_short(self):
        self.assertEqual(codewars.find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEqual(codewars.find_short("turns out random test cases are easier than writing out basic ones"), 3)
        self.assertEqual(codewars.find_short("lets talk about javascript the best language"), 3)
        self.assertEqual(codewars.find_short("i want to travel the world writing code one day"), 1)
        self.assertEqual(codewars.find_short("Lets all go on holiday somewhere very cold"), 2)

    def test_sum_two_smallest_numbers(self):
        self.assertEqual(codewars.sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        self.assertEqual(codewars.sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        self.assertEqual(codewars.sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

    def test_high_and_low(self):
        self.assertEqual(codewars.high_and_low("1 2 3 4 5"), "5 1")
        self.assertEqual(codewars.high_and_low("1 2 -3 4 5"), "5 -3")
        self.assertEqual(codewars.high_and_low("1 9 3 4 -5"), "9 -5")
        self.assertEqual(codewars.high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")

    def test_sum_array(self):
        # "None or Empty"
        self.assertEqual(codewars.sum_array(None), 0)
        self.assertEqual(codewars.sum_array([]), 0)
        # "Only one Element"
        self.assertEqual(codewars.sum_array([3]), 0)
        self.assertEqual(codewars.sum_array([-3]), 0)
        # "Only two Element"
        self.assertEqual(codewars.sum_array([3, 5]), 0)
        self.assertEqual(codewars.sum_array([-3, -5]), 0)
        # "Real Tests"
        self.assertEqual(codewars.sum_array([6, 2, 1, 8, 10]), 16)
        self.assertEqual(codewars.sum_array([6, 0, 1, 10, 10]), 17)
        self.assertEqual(codewars.sum_array([-6, -20, -1, -10, -12]), -28)
        self.assertEqual(codewars.sum_array([-6, 20, -1, 10, -12]), 3)

    def test_min_max(self):
        self.assertEqual(codewars.min_max([1, 2, 3, 4, 5]), [1, 5])
        self.assertEqual(codewars.min_max([2334454, 5]), [5, 2334454])
        self.assertEqual(codewars.min_max([1]), [1, 1])

    def test_high(self):
        self.assertEqual(codewars.high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(codewars.high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(codewars.high('take me to semynak'), 'semynak')

    def test_swap_vowels(self):
        self.assertEqual(codewars.swap_vowels("automation"), "oitamotuan")  # word with vowels
    #   self.assertEqual(codewars.swap_vowels("A23444U"), "U23444A")    # alphanumeric text with capital letter
        self.assertEqual(codewars.swap_vowels(""), "")  # empty text
        self.assertEqual(codewars.swap_vowels("i!888out"), "u!o888it")  # alphanumeric text with special character
        self.assertEqual(codewars.swap_vowels("text"), "text")  # word with only one vowel (no option for swap)
        self.assertEqual(codewars.swap_vowels("hello world"), "hollo werld")    # two words with vowels
        self.assertEqual(codewars.swap_vowels("rhythm"), "rhythm") # word with no vowels


if __name__ == '__main__':
    unittest.main()


