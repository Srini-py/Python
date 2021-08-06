'''
Given integers M and N, write a program that counts 
how many positive integer pairs (a, b) satisfy the following conditions:
a + b = M
a XOR b = N
'''


sum = int(input("Enter the sum of two numbers : "))
xor = int(input("Enter the xor of two numbers : "))
pairs = 0
for i in range(sum):
  if xor == (sum - i) ^ i:
    pairs += 1
    print("({0}, {1})".format(i, sum - i))

print("Total pairs are", pairs)