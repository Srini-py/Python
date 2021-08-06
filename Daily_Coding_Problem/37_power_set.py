# The power set of a set is the set of all its subsets. 
# Write a function that, given a set, generates its power set.

from itertools import combinations

def findCombinations(st, n):
    print({})
    for i in range(1, n + 1):
        print(*(set(i) for i in (combinations(st, i))))


st = list(map(int, input('Enter a set of integers :').split()))
findCombinations(st, len(st))