# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

def seperate_negative(arr):
        n = len(arr)
        j = 0
        for i in range(n):
                if arr[i] <= 0:
                        arr[i], arr[j] = arr[j], arr[i]
                        j += 1
        return j
    

def find_small_positive(a):
        n = len(a)
        for i in range(n):
                if abs(a[i]) - 1 < n and a[abs(a[i]) - 1] > 0:
                        a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]
        for i in range(n):
                if a[i] > 0:
                        return i + 1

        return n + 1


arr = [int(i) for i in input().split()]
n = len(arr)
print(find_small_positive(arr[seperate_negative(arr):]))


