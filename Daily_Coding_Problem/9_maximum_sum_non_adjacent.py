# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
# Numbers can be 0 or negative.

arr = [int(i) for i in input().split()]
n = len(arr)

incl = arr[0]
excl = 0

for i in range(1, n):
    temp = incl
    incl = excl + arr[i]
    excl = max(temp, excl)
    
print(max(incl, excl))