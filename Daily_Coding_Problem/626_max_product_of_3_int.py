import sys

def max_product(a):
  if len(a) < 3:
    return 'Error'
  
  maxA = -sys.maxsize - 1
  maxB = -sys.maxsize - 1
  maxC = -sys.maxsize - 1

  minA = sys.maxsize
  minB = sys.maxsize

  for i in a:
    if i > maxA:
      maxC = maxB
      maxB = maxA
      maxA = i
    elif i > maxB:
      maxC = maxB
      maxB = i
    elif i > maxC:
      maxC = i

    if i < minA:
      minB = minA
      minA = i
    elif i < minB:
      minB = i

  return max(minA * minB * maxA, maxA * maxB * maxC)


arr = [int(i) for i in input().split()]
m = max_product(arr)
if m != 'Error':
  print("Maximum product in the array is", m)
else:
  print("Insufficient Size")