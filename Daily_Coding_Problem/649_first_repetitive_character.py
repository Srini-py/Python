'''
Given a string, return the first recurring character in it, 
or null if there is no recurring character.
'''

string = input("Enter the string : ")
alphabet_hash = [0 for a in range(128)]
for char in string:
  alphabet_hash[ord(char)] += 1
  if alphabet_hash[ord(char)] > 1:
    print(char)
    break
else:
  print(None)