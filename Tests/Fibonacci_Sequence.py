"""

Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence
to that number or to the Nth number.

"""


def fibonacci_sequence(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a+b
    return

fibonacci_sequence(15)

