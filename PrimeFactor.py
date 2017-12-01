"""

Have the user enter a number and find all Prime Factors (if there are any) and display them

"""

import sys


def prime_factor(num):
    """

    :param num:
    :return:
    """
    i = 2
    list_of_factors = []
    while num > 1:
        if num % i == 0:
            list_of_factors.append(i)
            num /= i
            i -= 1
        i += 1
    return list_of_factors

#num = sys.argv[1:0]

#num = int(input("Enter the number to find the prime factors: "))
PrimeFactors = prime_factor(600851475143)
print(f'list of prime factors for 600851475143 are: ', PrimeFactors)

