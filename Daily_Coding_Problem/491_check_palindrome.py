'''
Write a program that checks whether an integer is a palindrome. 
'''


def check_palindrome(n):
  temp = n
  rev = 0
  while temp != 0 :
    rem = temp % 10
    rev = rev*10 + rem
    temp //= 10

  return n == rev


n = int(input("Enter the integer to check : "))
print(check_palindrome(n))