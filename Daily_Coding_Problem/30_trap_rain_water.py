# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.


def find_water(arr, n):
    left = [0] * n
    right = [0] * n
    water = 0
    
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])
    
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])
    
    for i in range(n):
        water += min(left[i], right[i]) - arr[i]
    
    return water
    
    

def trap_water(arr, n):
    low = 0
    high = n - 1
    left_max = 0
    right_max = 0
    res = 0
    while low < high:
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                res += left_max - arr[low]
            low += 1
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                res += right_max - arr[high]
            high -= 1
    return res



arr = [3, 0, 1, 3, 0, 5]
arr2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
n2 = len(arr)

trapped_water = find_water(arr, n)
water_count = trap_water(arr2, n2)
print("Maximum units of water trapped are :", trapped_water)
print("Maximum units of water trapped are :", water_count)