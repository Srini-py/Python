# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

def hash():
    return [0] * 26


def countUnique(string):
    count = hash()
    unq_char = 0
    for i in string:
        if not count[ord(i) - 97]:
            unq_char += 1
        count[ord(i) - 97] += 1
    return unq_char


def isValid(c, k):
    val = 0
    for i in range(26):
        if c[i] > 0:
            val += 1
            
    return k >= val


def findLongestSubstring(string, n):
    cur_win_start = cur_win_end = 0
    max_win_size = 1
    max_win_start = 0
    char_count = hash()
    char_count[ord(string[0]) - 97] = 1
    
    for i in string[1:]:
        char_count[ord(i) - 97] += 1
        cur_win_end += 1
        
        while not isValid(char_count, k):
            char_count[ord(string[cur_win_start]) - 97] -= 1
            cur_win_start += 1
            
        if cur_win_end - cur_win_start + 1 > max_win_size:
            max_win_size = cur_win_end - cur_win_start + 1
            max_win_start = cur_win_start
            
    return max_win_size, max_win_start


string = input("Enter a string :")
k = int(input("Enter the value of k :"))

n = len(string)

unq_char = countUnique(string)
if unq_char < k:
    print("Not enough characters")
else:
    win_size, win_start = findLongestSubstring(string, n)    
    print("Max substring is", string[win_start: win_start + win_size], "with length", win_size)
