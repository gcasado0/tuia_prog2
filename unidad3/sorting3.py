"""
3. Ordenamiento por selección

Dada una lista de n números enteros, el método de selección para ordenarlo en forma ascendente, es el
siguiente:
1. encontrar el menor valor de la lista (seleccionar el valor mínimo de la lista).
2. intercambiar el elemento encontrado con el primero de la lista.
3. repetir estas operaciones con los n − 1 elementos restantes, seleccionando, el segundo elemento, así
sucesivamente.
"""

def selectionSort(B):
    A=B[:]
    n = len(A)
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
        #intercambiar valores
        if posicion>i:
            A[posicion]=A[i]
            A[i]=minimo
    return A

        






