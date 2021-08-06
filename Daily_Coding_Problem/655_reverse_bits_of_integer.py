'''
Given a 32-bit integer, return the number with its bits reversed.
'''


n = int(input("Enter a 32-bit integer : "))
n_bin = bin(n)[2:]
reverse_bin = ''
for i in n_bin:
  if i == '0':
    reverse_bin += '1'
  else:
    reverse_bin += '0'

reverse_int = int(reverse_bin, 2)
print("The number with reversing bits is :", reverse_int)