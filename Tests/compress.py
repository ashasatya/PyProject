
#
# strng = "Reallly"
#
# lst_strng = list(strng)
# count = 0
# i = 0
# new_strng = []
#
# for i in range(0, len(strng)):
#     if lst_strng[i] != lst_strng[i+1]:
#         if count != 3:
#             new_strng.append(lst_strng[i])
#             i += 1
#             count += 1
#         # print(count)
#         else:
#             new_strng.append(str(count))
#             count += 1
#             i += 1
#     else:
#         continue
#
# print("".join(new_strng))
#
# def compress(s):
#     count=0
#
#     for i in range(0, len(s)):
#
#         if s[i] == s[i-1]:
#             print("Checking character", i, s[i])
#             count += 1
#             print("Found", s[i], c, "times")
#         c = s.count(s[i])
#
#
#     return str(s[i]) + str(c)
#
# print(compress("ddaaaff"))
#
# strng = "Reallly"
# # strng_lst = list(strng)
# count = 0
# new_strng = []
#
# for i in range(0, len(strng)):
#     print(strng[i])
#     if strng[i] == strng[i-1]:
#         count += 1
#         num_times = strng.count(strng[i])
#         new_strng.append(strng[i])
#         if num_times == 3:

strng = "Reallly"
count = 1
for i in range(1, len(strng) + 1):
    if i == len(strng):
        print(strng[i - 1] + str(count), end="")
        break
    else:
        if strng[i - 1] == strng[i]:
            count += 1
        else:
            print(strng[i - 1] + str(count), end="")
            count = 1
print("")


