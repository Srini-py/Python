'''
Given an array of integers, write a function to determine 
whether the array could become non-decreasing by modifying at most 1 element.
'''


array = [int(i) for i in input("Enter the array of elements : ").split()]

l = len(array)
chance_remains = 1
for i in range(l - 1):
  if array[i] > array[i + 1] and chance_remains:
    chance_remains -= 1
  elif array[i] > array[i + 1]:
    print("False")
    break
else:
  print("True")