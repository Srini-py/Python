# The edit distance between two strings refers to the minimum number of 
# character insertions, deletions, and substitutions required to change one string to the other. 
# For example, the edit distance between “kitten” and “sitting” is three: 
	# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.


def edit_distance(str1, str2, m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]



str1 = 'Sunday'
str2 = 'Saturday'

d = edit_distance(str1, str2, len(str1), len(str2))
print('The edit distance of {0} and {1} is {2}'.format(str1, str2, d))