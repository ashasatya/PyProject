import re
"""
Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater
than num1, otherwise return the string false. If the parameter values are equal to each other then return the string -1.
Sample Test Cases

Input:3 & num2 = 122
Output:true

Input:67 & num2 = 67
Output:-1
"""


def check_nums(num1, num2):

    if num1 == num2:
        return -1
    elif num1 < num2:
        return True
    else:
        return False

print(check_nums('100', '67'))
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
print(FirstFactorial(18))

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

print(TimeConvert(100))


def long_word(strng):
    word_list = re.sub("[^\w' ]", "", strng).split()
    longest_word = ''
    longest_size = 0
    for word in word_list:
        if len(word) > longest_size:
            longest_word = word
            longest_size = len(word)
    return longest_word

print(long_word("My name is Asha, my daughter is Sahana and my mom is Veena"))



