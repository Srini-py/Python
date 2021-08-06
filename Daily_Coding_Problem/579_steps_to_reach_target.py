'''
Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.
'''


def getsum(n):
  return n*(n+1)//2

end = int(input("Enter the number to reach : "))
ans = 0
while getsum(ans) < end or ((getsum(ans) - end) & 1):
  ans += 1

print(ans)