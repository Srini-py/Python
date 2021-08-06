# Given a stream of elements too large to store in memory, 
# pick a random element from the stream with uniform probability.

import random

def select_random(prev_val, val, tot):
    ans = random.choices([prev_val, val], weights = (tot - 1, 1), k = 1)
    return ans[0]



stream = [int(i) for i in input("Enter a stream of space seperated numbers :").split()]
n = len(stream)
current_choice = select_random(stream[0], stream[0], 1)
print("First number is", current_choice)
for i in range(1, n):
    current_choice = select_random(current_choice, stream[i], i + 1)
    print("Random number from first", i + 1, "numbers is", current_choice)
