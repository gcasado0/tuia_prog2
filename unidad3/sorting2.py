
#algoritmo: quicksort

def elegir_pivote(A):
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

def quicksortmia(A):
  if len ( A ) < 2:
    # Caso base : listas trivialmente ordenadas
    return A
  
  # Elegimos un pivote
  pivote = elegir_pivote ( A )
  # Usamos listas por comprensión para
  # obtener las sublistas que debemos ordenar
  
  menores = [ x for x in A if x < pivote]
  mayores = [ x for x in A if x > pivote]

  # Llamamos recursivamente a cada lado
  menores_ordenados = quicksortmia(menores)
  mayores_ordenados = quicksortmia(mayores)
  # Construimos la respuesta
  return menores_ordenados + [ pivote ] + mayores_ordenados
