
#algoritmo: quicksort

class Ordenar:
  
  def __init__(self):
    self.comparaciones = 0
    
  def reset(self):
    self.comparaciones = 0

  def elegir_pivote(self, A):
      if len(A)>2:
        a = A[0] #primero
        b = A[1] #segundo
        c = A[-1] #ultimo
        if  b < a and a < c:
          return a
        elif a < b and b < c:
          return b
        else:
          return c
      else:
        # Tecnica de elección a ciegas, elegimos siempre el primer elemento de la sublista a ordenar
        return A[0]

  def quickSort(self, A):
    if len ( A ) < 2:
      # Caso base : listas trivialmente ordenadas
      return A
    
    # Elegimos un pivote
    pivote = self.elegir_pivote(A)
    # Usamos listas por comprensión para
    # obtener las sublistas que debemos ordenar
    
    menores = [ x for x in A if x < pivote]#reemplazar por un for..
    mayores = [ x for x in A if x > pivote]

    self.comparaciones += len(A)

    # Llamamos recursivamente a cada lado
    menores_ordenados = self.quickSort(menores)
    mayores_ordenados = self.quickSort(mayores)
    # Construimos la respuesta
    return menores_ordenados + [ pivote ] + mayores_ordenados
