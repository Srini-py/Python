'''
Implement the function fib(n), which returns the nth number 
in the Fibonacci sequence, using only O(1) space.
'''


def fib(n):
  if n == 0 or n == 1:
    return 1

  a = i = 0
  b = 1
  while i < n - 1:
    b, a = a + b, b
    i += 1

  return b


n = int(input("Enter the value of n : "))
fib_n = fib(n)
print("The {0}th fibonacci number is {1}".format(n, fib_n))