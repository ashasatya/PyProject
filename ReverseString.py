#data = input("Enter the string to be reversed: ")
"""
Reverse a String - Enter a string and the program will reverse it and print it out.

"""


def reverse_string(my_string):
    new_string = []
    index = len(my_string)
    while index:
        index -= 1
        new_string.append(my_string[index])
    return ''.join(new_string)


print(reverse_string('what is the point of using a while loop here?'))

print('***********************************************')

data = 'what is the point of using a while loop here?'

print(data[::-1])

