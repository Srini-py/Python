# Given a string, find the longest palindromic contiguous substring. 
# If there are more than one with the maximum length, return any one.

def isPalindrome(l, h, s, n, i, mx):
    while l >= 0 and h < n and s[l] == s[h]:
        if h - l + 1 > mx:
            mx = h - l + 1
            i = l
        l -= 1
        h += 1
    return i, mx


def longestPalindrome(string):
    maxlength = 1
    start = 0
    n = len(string)
    
    for i in range(n):
        start, maxlength = isPalindrome(i - 1, i, string, n, start, maxlength)
        start, maxlength = isPalindrome(i - 1, i + 1, string, n, start, maxlength)
    print(f'The longest palindromic substring is {string[start: start + maxlength]}')


def longestPalindromeDP(s):
    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    maxlength = 1
    for i in range(n):
        dp[i][i] = 1
    
    start = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            start = i
            maxlength = 2
    
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = 1
                if k > maxlength:
                    start = i
                    maxlength = k
    print(f'Longest Palindromic Substring is {s[start: start + maxlength]} of length {maxlength}')


string = input('Enter a string : ')
longestPalindrome(string)
longestPalindromeDP(string)