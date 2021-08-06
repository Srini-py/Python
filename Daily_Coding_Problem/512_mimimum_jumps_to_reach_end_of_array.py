'''
You are given an array of nonnegative integers. 
Let's say you start at the beginning of the array and are trying to advance to the end. 
You can advance at most, the number of steps that you're currently on. 
Determine whether you can get to the end of the array(Minimum steps)
'''


def minjumps(arr, n):
  if n <= 1:
    return 0
  
  if arr[0] == 0:
    return -1

  maxreach = step = arr[0]
  jump = 1

  for i in range(1, n):
    if i == n - 1:
      return jump

    maxreach = max(maxreach, i + arr[i])
    step -= 1

    if step == 0:
      jump += 1
      if i >= maxreach:
        return -1

      step = maxreach - i
  
  return -1


arr = [int(i) for i in input("Enter the array of elements : ").split()]
length = len(arr)
jumps = minjumps(arr, length)
if jumps != -1:
  print("Minimum jumps required to reach end is :", jumps)
else:
  print("It is impossible to traverse to the end of the array")