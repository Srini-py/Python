# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

def decode(s, n):
    count = [0] * (n + 1)
    count[0] = count[1] = 1
    for i in range(2, n + 1):
        if s[i - 1] > '0':
            count[i] = count[i - 1]
        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
            count[i] += count[i - 2]
    return count[n]


code = input("Enter encoded message :")
print(decode(code, len(code)))
