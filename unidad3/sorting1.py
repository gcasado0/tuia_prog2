
"""
4. Ordenamiento por inserción
Dada una lista de n números enteros, el método de inserción para ordenarlo en forma ascendente, es el
siguiente:
1. Comenzamos considerando la sub-lista formado solo por el primer elemento. Esta lista esta trivialmente
ordenada.
2. Consideramos el siguiente elemento de la lista. En este momento, solo hay dos posibilidades, dado que
por simplicidad suponemos que no hay elementos repetidos:
  El elemento que vemos es menor que el primer elemento, y por lo tanto lo ubicamos a la izquierda
  del mismo.
  El elemento que vemos es mayor que el primer elemento, y por lo tanto lo ubicamos a la derecha
  del mismo.
3. Una vez realizado este, tenemos una sub-lista de tamaño dos ordenado. Repetimos para toda la secuen-
cia, en cada paso consideramos el siguiente elemento de la lista, y decidimos en que posición tenemos
que insertarlo
"""


def insertionsort(A):
  B = []
  for a in A:
    i = 0
    while i<len(B) and a>B[i]:
      i+=1
    B.insert(i,a)
  return B

def ordenar_por_insercion(B):
  A = B[:]
  # Guardamos en n la cantidad de elementos a ordenar
  n = len(A)
  for i in range (1,n):
    # Insertamos el elemento en la posición i
    value = A[i]
    j = i - 1
    while j >= 0:
      if value<A[j]:
        # Desplazamos el elemento en la posicion j
        # un lugar a la izquierda
        A[j+1]=A[j]
        j = j - 1
      else:
        break
    # Almacenamos el valor actual en el lugar que nos quedo disponible
    A[j+1]=value
  return A
