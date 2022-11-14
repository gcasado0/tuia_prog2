
#algoritmo: por insercion
def insertionsort(A):
  B = []
  for a in A:
    i = 0
    while i<len(B) and a>B[i]:
      i+=1
    B.insert(i,a)
  return B
