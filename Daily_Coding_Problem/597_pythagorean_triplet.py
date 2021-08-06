'''
Given an array of integers, determine whether it contains a Pythagorean triplet.
'''


def is_pythagorean(l, n):
  l = [i**2 for i in l]
  l.sort()
  for a in range(n - 1, 1, -1):
    b = 0
    c = a - 1
    while b < c:
      if l[b] + l[c] == l[a]:
        return True
      elif l[b] + l[c] < l[a]:
        b += 1
      else:
        c -= 1
  return False


list = [2, 4, 8, 15, 14, 16]
print(is_pythagorean(list, len(list)))