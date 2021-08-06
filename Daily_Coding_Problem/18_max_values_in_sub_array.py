# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

from collections import deque

def printmax(arr, k):
    n = len(arr)
    q = deque()
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k, n):
        print(arr[q[0]], end = ' ')
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    print(arr[q[0]])


arr = [int(i) for i in input("Enter an array of integers :").split()]
k = int(input("Enter the value of k :"))
printmax(arr, k)