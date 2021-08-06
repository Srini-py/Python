'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
'''


def max_contiguous_sum(arr):
  max_so_far = 0
  max_ending_here = 0
  for i in arr:
    max_ending_here += i
    if max_ending_here < 0:
      max_ending_here = 0

    elif max_so_far < max_ending_here:
      max_so_far = max_ending_here
  
  return max_so_far


array = [int(i) for i in input("Enter the array of elements : ").split()]
print("Maximum sum in the array is",max_contiguous_sum(array))