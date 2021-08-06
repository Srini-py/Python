# Suppose you are given a table of currency exchange rates, represented as a 2D array. 
# Determine whether there is a possible arbitrage: that is, 
# whether there is some sequence of trades you can make, starting with some amount A 
# of any currency, so that you can end up with some amount greater than A of that currency.


import sys


def arbitrage(g):
    log_graph = [[-log(edge) for edge in row] for row in g]
    src = 0
    n = len(g)
    min_dist = [sys.maxsize] * n
    min_dist[src] = 0
    
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + log_graph[v][w]:
                    min_dist = min_dist[v] + log_graph[v][w]
    
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + log_graph[v][w]:
                return True
    
    return False



curr_rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]

arbitrage(curr_rates)