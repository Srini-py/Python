'''
Given an array of integers in which two elements appear exactly once and 
all other elements appear exactly twice, find the two elements that appear only once.
'''


def non_repeating_elements(a):
  tot = 0
  for i in a:
    tot = (tot ^ i)
  
  tot = (tot & -tot)

  sum1 = 0
  sum2 = 0
  for i in a:
    if (tot & i) > 0:
      sum1 = (sum1 ^ i)
    else:
      sum2 = (sum2 ^ i)

  return sum1, sum2



arr = [int(i) for i in input("Enter an array of elements with 2 non repeating elements(repetition : 2 times)\n").split()]
a, b = non_repeating_elements(arr)
print("The non-repeating elements in the array are", a, b)