'''
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.
'''


arr = [int(i) for i in input("Enter the array of elements : ").split()]
product = 1
for i in arr:
  product *= i

arr = [product*(i**-1) for i in arr]
print(arr)