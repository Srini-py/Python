# Given an unordered list of flights taken by someone, 
# each represented as (origin, destination) pairs, and a starting airport, 
# compute the person's itinerary. If no such itinerary exists, return null. 
# If there are multiple possible itineraries, return the lexicographically smallest one. 
# All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
# and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

from collections import defaultdict

def createStationDictionary(flights):
    all_flights = defaultdict(list)
    for src, dest in flights:
        all_flights[src].append(dest)
    return all_flights


def itinerary(fd, src, n):
    in_degree = defaultdict(lambda: 0)
    for i in fd:
        for j in fd[i]:
            in_degree[j] += 1
    q = []
    q.append(src)
    count = 0
    top_order = []
    while q:
        u = q.pop(0)
        top_order.append(u)
        for i in fd[u]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
        count += 1
    if count != n:
        print('No Itinerary')
    else:
        print(top_order)


flight_list = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
src = 'YUL'
flights = createStationDictionary(flight_list)
itinerary(flights, src, 5)