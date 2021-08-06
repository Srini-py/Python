# Given an array of integers where every integer occurs three times except for one integer,
# which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.


def get_non_duplicate(arr, n):
    ones = 0
    twos = 0
    for i in arr:
        twos = twos ^ (ones & i)
        ones = ones ^ i
        mask = ~(ones & twos)
        ones &= mask
        twos &= mask
    return ones


arr = [int(i) for i in input('Enter an array with all but one element repeats thrice :').split()]
n = len(arr)
el = get_non_duplicate(arr, n)
print('The non duplicate element is', el)