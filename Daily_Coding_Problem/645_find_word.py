'''
Given a 2D matrix of characters and a target word, 
write a function that returns whether the word can be 
found in the matrix by going left-to-right, or up-to-down.
'''


rows, columns = map(int, input("Enter no.of rows and columns of the matrix :").split())
print("Enter the matrix :")
wordset1 = []
for _ in range(rows):
    wordset1.append(''.join(input().split()))

wordset2 = [''.join(word) for word in list(zip(*wordset1))]

key_word = input("Enter the target word to find :")

for word in wordset1:
    if key_word == word:
        print('True')
        break
else:
    for word in wordset2:
        if key_word == word:
            print('True')
            break
    else:
        print('False')