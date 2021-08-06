# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first, 
# the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.


def segregate(arr, n):
    cur_ind = 0
    pointer = 0
    while cur_ind < n:
        if arr[cur_ind] == 'R':
            arr[cur_ind], arr[pointer] = arr[pointer], arr[cur_ind]
            pointer += 1
        cur_ind += 1
    cur_ind = pointer
    while cur_ind < n:
        if arr[cur_ind] == 'G':
            arr[cur_ind], arr[pointer] = arr[pointer], arr[cur_ind]
            pointer += 1
        cur_ind += 1


arr = input('Enter an array of R, G, B\'s.').split()
segregate(arr, len(arr))
print(arr)