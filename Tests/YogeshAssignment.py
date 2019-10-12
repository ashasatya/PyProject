'''A = [1, 'yog', 10, 'Sana', 15, 'Asha', 'Veena']
B = []
C = []

for i in range(len(A)):
    try:
        lstValue = int(A[i])
        # print(str(A[i]) + ' Is an integer')
        B.append(A[i])

    except ValueError:
        # print(str(A[i]) + ' Is a string')
        C.append(A[i])


print(B)
print(C)
'''
""" ### THIS PROGRAM TAKES INPUT FROM USER and SORTS STRINGS AND INTEGERS to seperate list---- WORKS FINE
items = input("NUMBER of items in List: ")
myList = []
intList = []
strList = []
if int(items) != 0:
    for i in range(0, int(items)):
        myList.append(input())
        val = myList[i].isdigit() #---------- This command gives result when executed in pycharm
    #val = isinstance(myList[i], int) # This command gives result when executed in Terminal
    #print(val)
        if  val == True:
            intList.append(myList[i])
        else:
            strList.append(myList[i])
    print('STRING list: ', strList)
    print('INTEGER list: ', intList)
else:
    print("Your list is blank")


''' This is the program which works obsolutely fine'''
''' *****
for i in range(len(myList)):
    try:
        lstValue = int(myList[i])
        # print(str(A[i]) + ' Is an integer')
        intList.append(myList[i])

    except ValueError:
        # print(str(A[i]) + ' Is a string')
        strList.append(myList[i])

print('List of Integers: ', intList)

print('List of Strings: ', strList)
******* '''
'''
intList = [x for x in myList if isinstance(x, int)]
print(intList)
strList = [x for x in myList if isinstance(x, str)]
print(strList)
'''

'''
####
isinstance(),type(), isdigit(),isalpha(),
#####
'''

"""
import sys

items = sys.argv[1:]
#print(items)
strList = []
intList = []
if items != []:
    for val in items:
        if val.isdigit():
            intList.append(int(val))
        else:
            strList.append(val)

    print("Integer List: ", intList)
    print("String List: ", strList)
else:
    print("Rerun program and enter list items from terminal")

    #### This program fails when a negative number and float is passed
