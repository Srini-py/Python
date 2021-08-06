'''
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.
'''


def binarysearch(arr, l, r, k):
  if l > r:
    return -1
  
  mid = (l + r)//2
  if arr[mid] == k:
    return mid

  if arr[l] <= arr[mid]:
    if key >= arr[l] and key <= arr[mid]:
      return binarysearch(arr, l, mid - 1, k)
    return binarysearch(arr, mid + 1, r, k)

  if key >= arr[mid] and key <= arr[r]:
    return binarysearch(arr, mid + 1, r, k)
  return binarysearch(arr, l, mid - 1, k)


array = [int(i) for i in input("Enter the array of elements : ").split()]
key = int(input("Enter the key to search : "))
index = binarysearch(array, 0, len(array) - 1, key)
if index != -1:
  print("The element is present in index : ", index)
else:
  print("Element is not found")