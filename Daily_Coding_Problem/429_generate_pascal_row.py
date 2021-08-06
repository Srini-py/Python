'''
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
'''


def generate_pascal_row(n):
  prev = 1
  print(prev, end = ' ')
  for i in range(1, n):
    cur = (prev * (n - i))//i
    print(cur, end = ' ')
    prev = cur


n = int(input("Enter the row number in pascal triangle : "))
generate_pascal_row(n)