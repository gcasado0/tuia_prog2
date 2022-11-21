
def insertionSort(A, eficiencia):
  comparaciones = 0
  B = []
  for a in A:
    i = 0
    while i<len(B) and a>B[i]:
      i+=1
      comparaciones += 1
    B.insert(i,a)
  eficiencia.append(comparaciones)    
  return B

def insertionSortShift(B, eficiencia):
  A = B[:]
  # Guardamos en n la cantidad de elementos a ordenar
  n = len(A)
  comparaciones = 0
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
        comparaciones += 1
      else:
        break
    # Almacenamos el valor actual en el lugar que nos quedo disponible
    A[j+1]=value
  
  eficiencia.append(comparaciones)
  return A
