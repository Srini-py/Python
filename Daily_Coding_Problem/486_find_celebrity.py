'''
At a party, there is a single person who everyone knows, 
but who does not know anyone in return (the "celebrity"). 
To help figure out who this is, you have access to an O(1) method called knows(a, b), 
which returns True if person a knows person b, else False.

Given a list of N people and the above operation, 
find a way to identify the celebrity in O(N) time.
'''


matrix =  [
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]
          ]


def knows(a, b):
  return matrix[a][b]


def findcelebrity(matrix, n):
  a = 0
  b = n - 1

  while a < b:
    if knows(a, b):
      a += 1
    else:
      b -= 1

  for i in range(n):
    if (i != a) and (knows(a, i) or (not knows(i, a))):
      return -1
    
  return a


celeb = findcelebrity(matrix, len(matrix))

if celeb != -1:
  print("Celebrity ID is", celeb)
else:
  print("There is no celebrity")