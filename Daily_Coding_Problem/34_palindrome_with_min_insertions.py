# Given a string, find the palindrome that can be made by inserting the fewest number 
# of characters as possible anywhere in the word. 
# If there is more than one palindrome of minimum length that can be made, 
# return the lexicographically earliest one (the first one alphabetically)


def findMinInsertions(s, n):
    dp = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(1, n):
        l = 0
        for h in range(i, n):
            if s[l] == s[h]:
                dp[l][h] = dp[l + 1][h - 1]
            else:
                dp[l][h] = min(dp[l + 1][h], dp[l][h - 1]) + 1
            l += 1
    return dp[0][n - 1]


def isPalindrome(string):
    return string[::-1] == string


def findPalindrome(s):
    if isPalindrome(s):
        return s
    
    if s[0] == s[-1]:
        return s[0] + findPalindrome(s[1:-1]) + s[-1]
    else:
        pal1 = s[0] + findPalindrome(s[1:]) + s[0]
        pal2 = s[-1] + findPalindrome(s[:-1]) + s[-1]
        
        if len(pal1) < len(pal2):
            return pal1
        elif len(pal1) > len(pal2):
            return pal2
        return pal1 if pal1 < pal2 else pal2


string = input("Enter the string :")
print(findMinInsertions(string, len(string)))
print(findPalindrome(string))