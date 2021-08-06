'''
Given a string, determine whether any permutation of it is a palindrome.
'''


def checkpalindrome(s, n):
  l = []
  for char in s:
    if char in l:
      l.remove(char)
    else:
      l.append(char)
  
  if n%2 == 0 and len(l) == 0 or n%2 == 1 and len(l) == 1:
    return True
  else:
    return False


string = input("Enter the string : ")
print(checkpalindrome(string, len(string)))