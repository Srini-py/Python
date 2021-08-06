'''
Given a real number n, find the square root of n.
'''


def find_square_root(n):
  num = 0
  while num*num < n:
    num += 1
  
  if num*num == n:
      return num

  num -= 1

  for i in range(1, 5):
    for j in range(1, 10):
      temp = num + j/(10**i)
      if temp * temp > n:
        num += (j - 1)/(10**i)
        break

  return num


n = float(input("Enter a number : "))
root = find_square_root(n)
print("Square root of {0} is {1}".format(n, root))