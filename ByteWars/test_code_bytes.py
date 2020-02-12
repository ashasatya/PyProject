'''
Unit test suite for following functions
1. SimpleSymbols
2. Replace every letter in the string with the letter following it in the alphabet
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this
modified string.
3. Given a String of length S, reverse the whole string without reversing the individual words in it.
Words are separated by dots.
4. For this challenge you will be determining the largest word in a string.
5.  return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
Separate the number of hours and minutes with a colon.


'''

import unittest
import HtmlTestRunner
import code_bytes


class Testcoderbytes(unittest.TestCase):

    def test_SimpleSymbols(self):
        self.assertEqual(code_bytes.SimpleSymbols("+d+=3=+s+"), True)

    def test_LetterChanges(self):
        self.assertEqual(code_bytes.LetterChanges("hello*3"), "Ifmmp*3")
        self.assertEqual(code_bytes.LetterChanges("fun times!"), "gvO Ujnft!")

    def test_reverse_string(self):
        self.assertEqual(code_bytes.reverse_string("my.name.is.asha"), 'asha.is.name.my')

    def test_long_word(self):
        self.assertEqual(code_bytes.long_word("My name is Asha, my daughter is Sahana and my mom is Veena"), "daughter")
        self.assertEqual(code_bytes.long_word("Sahana is very beautiful and smart*&%$$####"), "beautiful")

    # def test_TimeConvert(self):
    #     self.assertEqual((code_bytes.TimeConvert(63), "1:3"))


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
