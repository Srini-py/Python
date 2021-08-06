# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
# implement a function rand7() that returns an integer from 1 to 7 (inclusive).

import random

def rand5():
    return random.randint(1, 5)


def rand7():
    val = 5 * rand5() + rand5() - 5
    if val < 22:
        return 1 + val % 7
    return rand7()


print(rand7())