"""
Given a string S. The task is to print all permutations of a given string.

"""


s = "AB"

if len(s) == 0 or len(s) == 1:
    print(s)
perm_list = []

for a in