# Implement regular expression matching with the following special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element

# That is, implement a function that takes in a string and a valid regular expression and 
# returns whether or not the string matches the regular expression.



def regex_matcher(pat, exp, m, n):
    if n == 0:
        return m == 0
    
    lookup = [[False for i in range(n + 1)] for j in range(m + 1)]
    lookup[0][0] = True
    
    for i in range(1, n + 1):
        if exp[i - 1] == '*':
            lookup[0][i] = lookup[0][i - 1]
            
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if exp[j - 1] == '*':
                lookup[i][j] = lookup[i - 1][j] or lookup[i][j - 1]
            elif exp[j - 1] == '.' or pat[i - 1] == exp[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]
            else:
                lookup[i][j] = False
    return lookup[m][n]


string = 'rayfrretyu'
regex = '.ra*.u'
print(regex_matcher(string, regex, len(string), len(regex)))
