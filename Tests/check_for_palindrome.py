"""

Check if Palindrome - Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”

"""


def check_palindrome(my_string):
    """

    :param my_string:
    :return:
    """
    index = len(my_string)
    #new_string = my_string[::-1]
    new_string = []
    while index:
        index -= 1
        new_string.append(my_string[index])
    new_string = ''.join(new_string)
    if my_string == new_string:
        print(f'{my_string} is a palindrome')
    else:
        print(f'{my_string} is NOT a palindrome')
    return


check_palindrome('hello')



