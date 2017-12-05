"""

Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads

"""
import sys
import random


def coinflip(num):
    """

    :param num:
    :return:
    """
    flip_list, heads, tails = [], 0, 0

    for i in range(num):
        flip = random.randint(0,1)
        if flip == 0:
            heads += 1
            flip_list.append("Heads")
        else:
                        flip_list.append("Tails")
    print(flip_list)
    print(f'Number of times heads displayed is {heads}')
    tails = num - heads
    print(f'Number of times tails displayed is {tails}')
    return

flip_times = sys.argv[1:]
if flip_times != []:
    tosses = flip_times[0]
    coinflip(int(tosses))
else:
    print('Rerun the program from the terminal and enter the number of time to flip the coin')