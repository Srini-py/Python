'''
Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
'''


def find_consecutive(arr, n):
  ans = 0
  s = set()
  for i in arr:
    s.add(i)

  for i in range(n):
    if arr[i]-1 not in s:
      j = arr[i]
      count = 0
      while j in s:
        j += 1
        count += 1

      ans = max(ans, count)
  
  return ans


arr = [int(i) for i in input("Enter the array of elements : ").split()]
print("No.of consecutive elements in array are",find_consecutive(arr, len(arr)))