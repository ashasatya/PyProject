"""
SimpleSymbols(str)
Input:"+d+=3=+s+"
Output:true

Input:"f++d+"
Output:false
"""
import re
import random


def SimpleSymbols(str):
    alpha_str = "abcdefghijklmnopqrstuvwxyz"

    if len(str) < 3:
        return False
    if (str[0] in alpha_str) or (str[-1] in alpha_str):
        return False
    for letter in range(1, len(str)-1):
        if str[letter] in alpha_str:
            if not (str[letter-1] == "+" and str[letter+1] == "+"):
                return False
    return True

# print(SimpleSymbols("=d+=3=+s+"))

"""

Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each 
word. Words will be separated by only one space.
Sample Test Cases

Input:"hello world"
Output:Hello World

Input:"i ran there"
Output:I Ran There
"""


def LetterCapitalize(str):
    new_str = str.split(" ")
    capitalized_str = []
    for word in new_str:
        capitalized_str.append(word.capitalize())
    return " ".join(capitalized_str)

# print(LetterCapitalize("hello world"))

"""
Given a String of length S, reverse the whole string without reversing the individual words in it.
Words are separated by dots.

"""


def reverse_string(strng):

    new_strng = strng.split(".")
    i = 0
    j = len(new_strng) -1

    while i < j:
        new_strng[i], new_strng[j] = new_strng[j], new_strng[i]
        i += 1
        j -= 1
    return ".".join(new_strng)

#print(reverse_string("this.is.sahana's.mom.my.name.is.asha"))

"""
Have the function LetterChanges(str) take the str parameter being passed and modify 
it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet 
(ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this 
modified string.
Sample Test Cases

Input:"hello*3"
Output:Ifmmp*3

Input:"fun times!"
Output:gvO Ujnft!
"""


def LetterChanges(str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    output_list = []
    final_list = []

    for letter in str:
        if letter in alphabets:
            new_letter = chr(ord(letter)+1)
            output_list.append(new_letter)
        else:
            output_list.append(letter)

    new_strng = "".join(output_list)
    for letter in new_strng:
        if letter in vowels:
            final_list.append(letter.upper())
        else:
            final_list.append(letter)
    return "".join(final_list)

#print(LetterChanges("hello*3 world!31"))

"""
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. 
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. 
For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Sample Test Cases

Input:4
Output:24

Input:8
Output:40320
"""


def FirstFactorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial
#print(FirstFactorial(18))

"""
Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the 
parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon.
Sample Test Cases

Input:126
Output:2:6
    
Input:45
Output:0:45
"""


def TimeConvert(num):
    minutes = num % 60
    hours = int(num / 60)

    return f'{hours}:{minutes}'

print(type(TimeConvert(100)))

"""
Longest word in the string along with removing the special characters
"""


def long_word(strng):
    word_list = re.sub("[^\w' ]", "", strng).split()
    longest_word = ''
    longest_size = 0
    for word in word_list:
        if len(word) > longest_size:
            longest_word = word
            longest_size = len(word)
    return longest_word

"""
FizzBuZZ sequence

"""

for i in range(1, 20):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuZZ")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""
Coin flip and return the number of times Heads and Tails appear

"""


def flip_coin(num):
    flip_list, heads, tails = [], 0, 0
    for i in range(20):
        flip = random.randint(0, 1)
        if flip == 0:
            heads += 1
            flip_list.append("Heads")
        else:
            tails += 1
            flip_list.append("Tails")
    print("Heads appeared:" f'{heads}' "times")
    print("Tails appeared:" f'{tails}' "times")
    return flip_list

"""
String Palindrome
"""


def palindrome(strng):
    rev_strng = strng[::-1]
    if strng == rev_strng:
        print("string is a palindrome")
    else:
        print("string is not a palindrome")


# palindrome("hello")

"""
Fibonacci Sequence
"""


def fibonacci_seq(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a + b
    return


# fibonacci_seq(10)

"""
Prime Factor for a number
"""


def prime_factor(num):
    i = 2
    list_primefactor = []
    while num > 1:
        if num % i == 0:
            list_primefactor.append(i)
            num /= i
            i -= 1
        i += 1
    return list_primefactor


# print(prime_factor(100))





