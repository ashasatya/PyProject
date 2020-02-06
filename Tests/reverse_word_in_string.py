"""
Given a String of length S, reverse the whole string without reversing the individual words in it.
Words are separated by dots.

"""


def rev_word_string(string):
    new_string = string.split(".")
    i = 0
    j = len(new_string) - 1

    while i < j:
        new_string[i], new_string[j] = new_string[j], new_string[i]
        i += 1
        j -= 1
    return ".".join(new_string)


print(rev_word_string("this.is.sahana's.mom.my.name.is.asha"))
print(rev_word_string("i.like.this.program.very.much"))