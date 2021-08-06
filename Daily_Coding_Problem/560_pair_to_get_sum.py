'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
'''

a, b = map(int, input().split())
arr = [int(i) for i in input().split()]
hashmap = set()
for i in arr:
  if not b - i in hashmap:
    hashmap.add(i)
  else:
    print(i, k - i)
    break