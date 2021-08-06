# Given an array of time intervals (start, end) for classroom lectures 
# (possibly overlapping), find the minimum number of rooms required.

def minRooms(arr):
    start_times = []
    end_times = []
    for start, end in arr:
        start_times.append(start)
        end_times.append(end)
    start_times.sort()
    end_times.sort()
    
    sx = ex = max_rooms = curr_rooms = 0
    while sx < len(start_times):
        if start_times[sx] < end_times[ex]:
            curr_rooms += 1
            sx += 1
        else:
            curr_rooms -= 1
            ex += 1
        max_rooms = max(max_rooms, curr_rooms)
    return max_rooms
    

def minRooms2(arr):
    time_counter = [0 for i in range(1441)]
    for i in arr:
        time_counter[i[0]] += 1
        time_counter[i[1]] -= 1
    rooms = tmp = 0
    for i in time_counter:
        tmp += i
        if tmp > rooms:
            rooms = tmp
    return rooms



arr = [(30, 75), (0, 50), (60, 150)]
arr2 = [(1, 3), (5, 8), (4, 10), (20, 25)]
print(minRooms(arr2))
print(minRooms2(arr2))