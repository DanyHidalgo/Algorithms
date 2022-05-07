'''
Binary Search algorithm
'''

def binary_search(lista, n, elemento_buscado):
    
  menor = 0
  mayor = n - 1
  mitad = 0

  while menor <= mayor:
    
    mitad = (mayor + menor) // 2

    if lista[mitad] < int(elemento_buscado):
      
      menor = mitad + 1

    elif lista[mitad] > int(elemento_buscado):
      
      mayor = mitad - 1

    else:
      
      return mitad

  return -1