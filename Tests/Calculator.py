"""

Calculator - A simple calculator to do basic operators.
Make it a scientific calculator for added complexity.

"""


def addition(a, b):
    total = a + b
    return total


def subtraction(a, b):
    value = a - b
    return value


def division(a, b):
    value = a / b
    return value


def multiplication(a, b):
    value = a * b
    return value

a = 200
b = 30
add_value = addition(a, b)
sub_value = subtraction(a, b)
division_value = division(a, b)
multiply_value = multiplication(a, b)

print(f'When {a} and {b} are ADDED:{add_value}, SUBTRACTED:{sub_value}, '
      f'DIVIDED:{division_value}, and MULTIPLIED:{multiply_value}')