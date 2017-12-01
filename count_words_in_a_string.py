"""

Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.

"""


def count_words_in_string(my_string):
    """

    :param my_string:
    :return:
    """
    word_count = 1
#    new_list = my_string.split(' ')
    index = len(my_string)
    for i in range(index):
        if my_string[i] == ' ':
            word_count += 1
        else:
            continue
    return word_count


cw = count_words_in_string('My name is Asha, my daughter is Sahana and my mom is Veena')
print(cw)
