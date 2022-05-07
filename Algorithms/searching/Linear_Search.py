'''
Linear Search algorithm
'''

def Search(lista, key):
  
  for i in range(len(lista)):
  
    if key == lista[i]:
      return i
  return -1
