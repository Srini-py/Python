'''
Implement division of two positive integers without using the 
division, multiplication, or modulus operators. 
Return the quotient as an integer, ignoring the remainder.
'''

a, b = map(int, input("Enter the two numbers : ").split())
quotient = 0
if a > 0:
  while a >= b:
    a = a - b
    quotient += 1
else:
  while a < 0:
    a = a + b
    quotient -= 1
print(quotient)