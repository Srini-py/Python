'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
'''


def printspiral(matrix, i, m, n):
  if i >= m or i >= n:
    return
  
  for p in range(i, n):
    print(matrix[i][p], end = " ")
  
  for p in range(i + 1, m):
    print(matrix[p][n-1], end = " ")

  if (m - 1) != i:
    for p in range(n - 2, i - 1, -1):
      print(matrix[m-1][p], end = " ")

  if (n - 1) != i:
    for p in range(m - 2, i, -1):
      print(matrix[p][i], end = " ")

  printspiral(matrix, i + 1, m - 1, n - 1)
  

r, c = map(int, input("Enter no.of rows and columns in the matrix :").split())
matrix = [[c*i + j for j in range(1, c+1)] for i in range(r)]
printspiral(matrix, 0, r, c)