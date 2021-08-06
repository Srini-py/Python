'''
Given a string of parentheses, find the balanced string that can be produced from it 
using the minimum number of insertions and deletions. 
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
'''


s = input("Enter unbalanced parantheses : ")
counter = 0
res = ''
for c in s:
  if c == '(':
    res += '('
    counter += 1
  else:
    if counter == 0:
      res += '('
    else:
      counter -= 1
    res += ')'

while counter > 0:
  res += ')'
  counter -= 1

print("Balanced parantheses expression is : "+res)