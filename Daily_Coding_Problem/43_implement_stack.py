# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack

# pop(), which pops off and returns the topmost element of the stack. 
# If there are no elements in the stack, then it should throw an error or return null.

# max(), which returns the maximum value in the stack currently. 
# If there are no elements in the stack, then it should throw an error or return null.

# Each method should run in constant time.

import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.max_el = -sys.maxsize - 1
        self.cur_size = 0
    
    def push(self, val):
        if self.cur_size == 0:
            self.stack.append(val)
            self.max_el = val
        else:
            if val <= self.max_el:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.max_el)
                self.max_el = val
        self.cur_size += 1
    
    def pop(self):
        if self.cur_size == 0:
            return None
        top = self.stack.pop()
        self.cur_size -= 1
        if top > self.max_el:
            maxi = self.max_el
            self.max_el = 2 * self.max_el - top
            return maxi
        else:
            return top
    
    def max(self):
        if self.cur_size == 0:
            return None
        return self.max_el


st = Stack()
st.push(20)
st.push(40)
st.push(30)
st.push(41)
st.push(15)
st.push(81)
print(st.max())
print(st.pop())
st.push(29)
print(st.max())
