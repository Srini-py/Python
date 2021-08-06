'''
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
'''


string1, string2 = input("Enter the two strings to map :").split()
freq1 = [0 for i in range(128)]
for char in string1:
  freq1[ord(char)] += 1
freq_str1 = ''
for i in freq1:
  if i > 0:
    freq_str1 += str(i)
freq_str1 = ''.join(sorted(freq_str1))

freq2 = [0 for i in range(128)]
for char in string2:
  freq2[ord(char)] += 1
freq_str2 = ''
for i in freq2:
  if i > 0:
    freq_str2 += str(i)
freq_str2 = ''.join(sorted(freq_str2))
print(freq_str1 == freq_str2)