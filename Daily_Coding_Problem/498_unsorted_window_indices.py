'''
Given an array of integers out of order, 
determine the bounds of the smallest window that must be sorted 
in order for the entire array to be sorted.
'''


def find_unsorted_window_indices(arr, n):
  i = 0
  start = end = 0
  while i < n - 1:
    if arr[i] > arr[i+1]:
      start = i
      break
    i += 1

  j = n - 1
  while j > 0:
    if arr[j] < arr[j - 1]:
      end = j
      break
    j -= 1

  maxi = max(arr[start : end + 1])
  mini = min(arr[start : end + 1])

  for i in range(start):
    if arr[i] > mini:
      start = i
      break
    
  for i in range(n - 1, end, -1):
    if arr[i] < maxi:
      end = i
      break

  return start, end


arr = [int(i) for i in input("Enter the array of elements : ").split()]
start, end = find_unsorted_window_indices(arr, len(arr))
print("Unsorted window is ({0}, {1})".format(start, end))