# Given a list of integers S and a target number k, 
# write a function that returns a subset of S that adds up to k. 
# If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. 
# You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.


#Recursive Solutions
def findSubsetSum(arr, n, sum):
    if sum == 0:
        return True
    elif n == 0:
        return False
    if arr[n - 1] > sum:
        return findSubsetSum(arr, n - 1, sum)
    return findSubsetSum(arr, n - 1, sum) or findSubsetSum(arr, n - 1, sum - arr[n - 1])


def findSubsets(arr, n, v, sum):
  if sum == 0:
    print(v)
    return
  if n == 0:
    return
  findSubsets(arr, n - 1, v, sum)
  v1 = [] + v
  v1.append(arr[n - 1])
  findSubsets(arr, n - 1, v1, sum - arr[n - 1])


#Dynamic Programming
def isSubsetSumDP(arr, n, sum):
    dp = [[False for j in range(sum + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, sum + 1):
        dp[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])
    return dp[n][sum]


def isSubsetSumDPOpt(arr, n, sum):
    dp = [False] * (sum + 1)
    dp[0] = True
    for i in range(n):
        for j in range(sum, arr[i] - 1, -1):
            if dp[j - arr[i]]:
                dp[j] = True
    return dp[sum]


arr = [int(i) for i in input('Enter array of space seperated elements :').split()]
sum = int(input('Enter a sum :'))
size = len(arr)
# print(findSubsetSum(arr, size, sum))
# print(isSubsetSumDP(arr, size, sum))
# print(isSubsetSumDPOpt(arr, size, [], sum))
# findSubsets(arr, size, [], sum)