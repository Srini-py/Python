# We can determine how "out of order" an array A is by counting the number of inversions it has. 
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. 
# That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            i += 1
        else:
            j += 1
            inv_count += (mid - i + 1)
    return inv_count


def mergesort(arr, left, right):
    inv_count = 0
    if right > left:
        mid = left + (right - left) // 2
        inv_count += mergesort(arr, left, mid)
        inv_count += mergesort(arr, mid + 1, right)
        inv_count += merge(arr, left, mid, right)
    return inv_count


arr = [int(i) for i in input('Enter an array of integers :').split()]
n = len(arr)

res = mergesort(arr, 0, n - 1)
print(res)