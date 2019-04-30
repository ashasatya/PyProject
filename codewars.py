
'''
print(longest("wieuiwejdasjkdhasj", "uyehhgsdhsgdgsd"))
print(validate_pin('123456'))
print(toJadenCase("Vince Staples officially has a life time supply of water")
print(find_short("Lets all go on holiday somewhere very cold"))
print(sum_two_smallest_numbers([25, 12, 12, 18, 22]))
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))  # return "5 1"
print(positive_sum([-1,-2,-3,-4,5]))
'''


def high_and_low(numbers):
    # ...
    numbers_list = numbers.split(' ')
    nums = sorted(numbers_list, key=int)
    return f'{nums[-1]} {nums[0]}'


def positive_sum(arr):
    sum = 0
    for value in arr:
        if value > 0:
            sum = sum + value
    return sum


def sum_two_smallest_numbers(numbers):
    num_sort = sorted(numbers)
    total = num_sort[0]+num_sort[1]
    return total


def find_short(s):
    s_list = s.split(' ')
    sort_slist = sorted(s_list, key=len)
    l = len(sort_slist[0])
    return l


def toJadenCase(string):
    # ...
    jaden_case = []
    str_lst = string.split(' ')
    for i, val in enumerate(str_lst):
        jc = str_lst[i].capitalize()
        jaden_case.append(jc)
        jadencase = ' '.join(jaden_case)
    return jadencase
#   print(toJadenCase("Vince Staples officially has a life time supply of water"))


def grow(arr):
    mul_val = 1
    for i, val in enumerate(arr):
        mul_val = mul_val*arr[i]
    return mul_val


def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        val = True
    else:
        val = False
    return val


def longest(s1, s2):
    return ''.join(sorted(set(list(s1+s2))))


def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


def min_max(lst):
    new_lst = []
    new_lst.append(min(lst))
    new_lst.append(max(lst))
    return new_lst

word_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,'v': 22,'w': 23, 'x': 24,
            'y': 25, 'z': 26}


def high(sentence):

    lcase_sentence = sentence.lower()  # convert the text to a lower case
    word_lst = lcase_sentence.split(' ')   # convert the string into the list of words
    weight_lst = []
    for x, word in enumerate(word_lst):
        weight = 0
        char_lst = list(word_lst[x])    # convert words into a list of characters
        for i, char in enumerate(char_lst):
            weight += word_dictionary.get(char)     # add weight by referring to the dictionary
        weight_lst.append(weight)      # append the weight list with the weight
#   print(weight_lst)
    score = max(weight_lst)     # get the max value from the weight list
    output = dict(zip(weight_lst, word_lst))    # merge two lists to a new dictionary
    return output[score]    # return the value of the max weight from dictionary

#   print(high('iriwhopsrs jmshiozlsw'))










