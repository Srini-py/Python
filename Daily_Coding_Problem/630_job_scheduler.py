'''
Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.
'''

import time

def schedule(fnc, milliseconds):
  time.sleep(milliseconds/1000)
  fnc()

def out():
  print("Hello World")

for i in range(10):
  schedule(out, 100)