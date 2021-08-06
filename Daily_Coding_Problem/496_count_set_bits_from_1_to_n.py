 '''
Write an algorithm that finds the total number of set bits in all integers between 1 and N.
'''


def count_set_bits(n):
  set_bits = [0 for i in range(n + 1)]
  count = 0
  set_bits[0] = 0
  set_bits[1] = 1

  for i in range(2, n + 1):
    if i%2 == 0:
      set_bits[i] = set_bits[i//2]
    else:
      set_bits[i] = 1 + set_bits[i - 1]

  for i in range(1, n + 1):
    count += set_bits[i]

  return count


n = int(input("Enter the value of N : "))
print("Total set bits from 1 to {} are :".format(n), count_set_bits(n))