# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. 
# If there is more than one possible reconstruction, return any of them. 
# If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
# you should return ['the', 'quick', 'brown', 'fox'].


stack = []

def wordBreak(words, string):
    wordList = words[:]
    n = len(string)
    if n == 0:  return True
    dp_list = [0] * n
    matched_index = [-1]
    for i in range(n):
        msize = len(matched_index)
        flag = 0
        for j in range(msize - 1, -1, -1):
            sb = string[matched_index[j] + 1: i + 1]
            if sb in words:
                flag = 1
                words.remove(sb)
                break
        if flag == 1:
            dp_list[i] = 1
            matched_index.append(i)
    for i in range(1, len(matched_index)):
      for j in range(i - 1, -1, -1):
        if string[matched_index[j] + 1: matched_index[i] + 1] in wordList:
          stack.append(string[matched_index[j] + 1:matched_index[i] + 1])
          break
        else:
          stack.pop()
    return stack


def canWordBreak(wordList, word):
  if not word:
    return True
  wordLen = len(word)
  return any([(word[:i] in wordList) and canWordBreak(wordList, word[i:]) for i in range(1, wordLen + 1)])


words = input('Enter space seperated words : ').split()
string = input('Enter the string to parse : ')
res2 = canWordBreak(words, string)
res = wordBreak(words, string)
print(res2)
print(res)