# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

arr = [int(i) for i in input().split()]
temp = 1
n = len(arr)
prod = [1 for i in range(n)]
for i in range(n):
    prod[i] = temp
    temp *= arr[i]

temp = 1

for i in range(n - 1, -1, -1):
    prod[i] *= temp
    temp *= arr[i]
    
print(prod)
