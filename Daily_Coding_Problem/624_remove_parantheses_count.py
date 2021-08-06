'''
Given a string of parentheses, write a function to compute the minimum 
number of parentheses to be removed to make the string valid.
'''

exp = input("Enter the string of parantheses : ")
remove = 0
state = None
start_state_count = 0
for par in exp:
  if par == '(':
    state = 'start'
    start_state_count += 1
  else:
    if state == None:
      remove += 1
    else:
      start_state_count -= 1
  
  if start_state_count == 0:
    state = None

print(remove + start_state_count)