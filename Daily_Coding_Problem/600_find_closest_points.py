'''
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points.
'''

from math import sqrt

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y


def dist(p1, p2):
  return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def brute_force(p, l):
  min = float('inf')
  for i in range(l):
    for j in range(i+1, l):
      if dist(p[i], p[j]) < min:
        min = dist(p[i], p[j])
        point1 = p[i]
        point2 = p[j]

  return point1, point2, min


def strip_closest(list, l, d, p1, p2):
  min_val = d
  list.sort(key = lambda p: p.y)
  for i in range(l):
    j = i + 1
    while j < l and (list[j].y - list[i].y) < min_val:
      min_val = dist(list[i], list[j])
      p1 = list[i]
      p2 = list[j]
      j += 1
    
  return p1, p2, min_val


def closest_pair(p, l):
  if l <= 3:
    return brute_force(p, l)
  
  mid = l//2
  mid_point = p[mid]

  p1, p2, dl = closest_pair(p[:mid], mid)
  p3, p4, dr = closest_pair(p[mid:], l - mid)
  if dl < dr:
    point1, point2 = p1, p2
    d = dl
  else:
    point1, point2 = p3, p4
    d = dr
  strip_list = []
  for i in range(l):
    if abs(p[i].x - mid_point.x) < d:
      strip_list.append(p[i])

  po1, po2, m = strip_closest(strip_list, len(strip_list), d, point1, point2)
  if d < m:
    return point1, point2, d
  else:
    return po1, po2, m


def closest(p, l):
  p.sort(key = lambda obj: obj.x)
  return closest_pair(p, l)


points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
length = len(points)
p1, p2, dis = closest(points, length)
print("The closest pair of points are :({0}, {1}) ({2}, {3}) with distance of {4}".format(p1.x, p1.y, p2.x, p2.y, dis))
