# Write an algorithm to justify text. Given a sequence of words and an integer line length k, 
# return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line. 
# There should be at least one space between each word. 
# Pad extra spaces when necessary so that each line has exactly length k. 
# Spaces should be distributed as equally as possible, with the extra spaces, 
# if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.


def word_wrap(words, n, l):
    index = 0
    while index < n:
        line_length = 0
        line_string = ''
        while line_length <= k:
            if index >= n:
                break
            line_length += l[index]
            if line_length > k:
                break
            line_string += words[index] + ' '
            line_length += 1
            index += 1
        print(line_string)


words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
k = 16

l = len(words)
len_words = [len(word) for word in words]
word_wrap(words, l, len_words)