# Given a string of round, curly, and square open and closing brackets, 
# return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


def balance(exp):
    stack = []
    
    for ch in exp:
        if ch in ['[', '{', '(']:
            stack.append(ch)
        else:
            if not stack:
                return False
            char = stack.pop()
            if char == '(':
                if ch != ')':
                    return False
            elif char == '{':
                if ch != '}':
                    return False
            elif char == '[':
                if ch != ']':
                    return False
    return not stack


def balance2(par):
  stack = []
  for ch in par:
    if ch in ['(', '[', '{']:
      stack.append(ch)
    else:
      if (stack[-1] == '(' and ch == ')') \
      or (stack[-1] == '[' and ch == ']') \
      or (stack[-1] == '{' and ch == '}'):
        stack.pop()
  return not bool(stack)


string = '[()]{}{[()()]()}'
print(balance(string))
print(balance2(string))