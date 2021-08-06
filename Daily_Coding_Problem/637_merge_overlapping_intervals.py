'''
Given a list of possibly overlapping intervals, 
return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
'''

no_of_intervals = int(input("Enter no.of intervals: "))

interval_list = []
for _ in range(no_of_intervals):
    interval_list.append(tuple(map(int,input("Enter interval {}: ".format(_ + 1)).split())))
    
interval_list.sort()
open, close = interval_list[0]
final_interval_list = [interval_list[0]]
for i in range(1, no_of_intervals):
    if open == interval_list[i][0]:
        del final_interval_list[-1]
        final_interval_list.append(interval_list[i])
    elif not close >= interval_list[i][1]:
        final_interval_list.append(interval_list[i])
    if close > interval_list[i][1]:
      open, close = interval_list[i]

print(final_interval_list)