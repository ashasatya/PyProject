"""

Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.


"""


def count_vowels(my_string):
    """
    
    :param my_string: 
    :return: 
    """
    index = len(my_string)
    vowels = 'aeiouAEIOU'
    count = 0
    #total = (count+1 for i in range(index) if my_string[i] in vowels)
    #return total

    for i in range(index):
        if my_string[i] in vowels:
            count = count + 1
        else:
            continue
    return count


cw = count_vowels('TestCalc')
print(cw)

'''

my_string = 'sahana is my daughter, veena is my mom'

vowels = 'aeiou'
x = 0
total = (len(x) for x in my_string if my_string[x] in vowels)

print(total)

'''