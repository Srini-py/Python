'''
The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.
'''


import random

iterate = 10**6
square_points = 0
circle_points = 0
for i in range(iterate):
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)

  area = x**2 + y**2
  if area < 1:
    circle_points += 1

  square_points += 1

pi = 4 * (circle_points/square_points)
print(pi)