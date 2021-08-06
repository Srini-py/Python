'''
It is conjectured that every such sequence eventually reaches the number 1. 
Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?
'''


def findcolseq(i, collatzmap):
  if i in collatzmap:
    return collatzmap[i]
  if i == 1:
    collatzmap[i] = 1
  elif i%2 == 0:
    collatzmap[i] = 1 + findcolseq(i//2, collatzmap)
  else:
    collatzmap[i] = 1 + findcolseq(3*i + 1, collatzmap)
  return collatzmap[i]


def collatz(n):
  collatzmap = {}
  findcolseq(n, collatzmap)
  num, l = -1, 0
  for i in range(1, n):
    if i not in collatzmap:
      findcolseq(i, collatzmap)
    seq_len = collatzmap[i]
    if l < seq_len:
      l = seq_len
      num = i
  return (num, l)


number = 1000000
print(collatz(number))