'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
'''

num = int(input("Enter the number : "))
count_1 = 0
max_1 = 0
while num != 0:
  if num %2 == 1:
    count_1 += 1
  else:
    if count_1 > max_1:
      max_1 = count_1
    count_1 = 0
  num = num // 2
else:
  if count_1 > max_1:
    max_1 = count_1

print(max_1)
