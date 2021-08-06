'''
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.
'''


def find_duplicate(arr, n):
  total = sum(arr)
  sum_to_n = n*(n + 1)//2
  return total - sum_to_n


arr = [int(i) for i in input("Enter n + 1 elements from 1 to n with a duplicate : ").split()]
n = len(arr) - 1
duplicate = find_duplicate(arr, n)
print("The duplicate element is", duplicate)