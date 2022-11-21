
def selectionSort(B):
    A=B[:]
    n = len(A)
    comparaciones = 0
    for i in range(n-1):
        #buscar el minimo
        j = i+1
        minimo=A[i]
        posicion = i
        while j<n:
            if A[j]<minimo:
                minimo = A[j]
                posicion = j
            j+=1
            comparaciones += 1
        #intercambiar valores
        if posicion>i:
            A[posicion]=A[i]
            A[i]=minimo
    return A, comparaciones
