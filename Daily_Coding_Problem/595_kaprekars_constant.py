'''
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
'''


str_num = input("Enter a four digit number with atleast 2 different digits : ")
num = int(str_num)
steps = 0
while num != 6174:
  print(num)
  asc = int(''.join(sorted(str_num)))
  desc = int(''.join(sorted(str_num, reverse = True)))
  num = desc - asc
  str_num = str(num)
  str_num = str_num if len(str_num) == 4 else '0'+str_num
  steps += 1

print(steps)