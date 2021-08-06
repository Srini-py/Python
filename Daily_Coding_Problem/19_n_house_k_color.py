# A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents 
# the cost to build the nth house with kth color, 
# return the minimum cost which achieves this goal.


no_of_houses = int(input("Enter the no.of houses :"))
no_of_colors = int(input("Enter the no.of colors :"))
house_cost = []
for i in  range(no_of_houses):
    house_cost.append([int(i) for i in input().split()])
cost_matrix = [[0 for i in range(no_of_colors)] for j in range(no_of_houses)]
cost_matrix[0] = house_cost[0]
for i in range(1, no_of_houses):
    for j in range(no_of_colors):
        cost_matrix[i][j] = house_cost[i][j] + min([cost_matrix[i - 1][p] for p in range(no_of_colors) if p != j])
print(min(cost_matrix[-1]))