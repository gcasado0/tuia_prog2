"""
Ejercicio 6: Dada una grilla, modelada como una lista de listas, 
donde "." representa suelo caminable, y "o" representa suelo no caminable, 
determine si hay un camino desde la celda  (0,0)  a la celda  (n−1,n−1)  
donde solamente nos movamos hacia la derecha o hacia abajo.

La celda  (0,0)  la consideramos arriba a la izquierda y la  (n−1,n−1)  la de abajo a la derecha.
Los valores en estas celdas son siempre caminables.
No nos movemos en ambas direcciones a la vez
Ayuda: Haga una recursión donde prueba ir por derecha y por abajo, use la posición actual como parámetro de la recursión
Como un extra, haga el algoritmo para que retorne la lista de celdas que son el camino a seguir.

"""
caso1 ="""
. o o . .
. o . . .
. . . o o
. . . . o
o o o . . 
"""
# SI

caso2 = """
. o . . .
. . . o .
. o o . .
. . o . o
o . o . . 
"""
# NO

from math import sqrt

#generalizar a un ancho y largo dados
class Grid:
  def __init__(self, string):
    raw_split = string.replace("\n", " ").replace("\t", " ").split(" ")

    self.cells = [symbol for symbol in raw_split if symbol != ""]
    
  def at(self, x, y):
    return self.cells[x + self.size() * y]

  def size(self):
    return int(sqrt(len(self.cells)))


def es_caso_base(x):#extender caso base para que incluya hasta 2 elementos
    if x == [] or x == [[]] or x[0][0] == "o" or x == [["."]]:
        return True
    return False

def resolver_caso_base(x):
    if x==[["."]]:
        return True
    return False
    
def dividir(lista):    
    abajo = lista[1:]
    derecha = []
    for fila in lista:
        derecha.append(fila[1:])
    return abajo, derecha

def combinar(s1, s2):
    return s1 or s2

def mostrar(grilla):    
    for fila in grilla:
        for x in fila:
            print(x,end="")
        print("")

def resolver(problema):
    if es_caso_base(problema):
        return resolver_caso_base(problema)

    p1, p2 = dividir(problema)
    s1 = resolver(p1)
    s2 = resolver(p2)
    if s1:
        print("abajo:")
        mostrar(p1)
    if s2:
        print("derecha:")
        mostrar(p2)

    return combinar(s1, s2)

#g1 = Grid(caso1)
#print(g1.cells)
g1 = [
[".","o","o",".","."],
[".","o",".",".","."],
[".",".",".","o","o"],
[".",".",".",".","o"],
["o","o","o",".","."]]

mostrar(g1)

s1 = resolver(g1)
print(s1)
#ver como mostrar todas las posibles soluciones...
