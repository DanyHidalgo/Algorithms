'''
A countdown from an n number
'''

from sys import setrecursionlimit, getrecursionlimit

def inf(n):
  
  setrecursionlimit(10000)

  getrecursionlimit()

  if n == 0:

      return 0

  print(n)
  
  return inf(n -1)
  
