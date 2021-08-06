# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

# Given this matrix, a start coordinate, and an end coordinate, 
# return the minimum number of steps required to reach the end coordinate from the start. 
# If there is no possible path, then return null. 
# You can move up, left, down, and right. 
# You cannot move through walls. You cannot wrap around the edges of the board.

import sys
from collections import deque

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]

def is_valid(mat, n, x, y, vis):
    return x >= 0 and x < n and y >= 0 and y < n and mat[x][y] == 'f' and (not vis[x][y])


def shortest_path(graph, n, start, end):
    start_x, start_y = start
    end_x, end_y = end
    
    q = deque()
    visited = [[0 for i in range(n)] for j in range(n)]
    
    visited[start_x][start_y] = 1
    q.append((start_x, start_y, 0))
    
    mindist = sys.maxsize
    
    while q:
        x, y, dist = q.popleft()
        
        if x == end_x and y == end_y:
            mindist = dist
            break
        
        for i in range(4):
            if is_valid(graph, n, x + row[i], y + col[i], visited):
                q.append((x + row[i], y + col[i], dist + 1))
                visited[x + row[i]][y + col[i]] = 1
    
    if mindist != sys.maxsize:
        print("The minimum distance from {0} to {1} is {2}".format(start, end, mindist))
    else:
        print("There is no path from {0} to {1}".format(start, end))



matrix = [
    ['f', 'f', 'f', 'f'],
    ['t', 't', 'f', 't'],
    ['f', 'f', 'f', 'f'],
    ['f', 'f', 'f', 'f']
]

start = (3, 0)
end = (0, 0)

shortest_path(matrix, len(matrix), start, end)
