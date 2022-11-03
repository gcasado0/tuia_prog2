"""
Ejercicio 6: Dada una grilla, modelada como una lista de listas, donde "." representa suelo caminable, 
y "o" representa suelo no caminable, determine si hay un camino desde la celda  (0,0)  a la celda  (n−1,n−1)  
donde solamente nos movamos hacia la derecha o hacia abajo.

La celda  (0,0)  la consideramos arriba a la izquierda y la (n−1,n−1) la de abajo a la derecha.
Los valores en estas celdas son siempre caminables.
No nos movemos en ambas direcciones a la vez

. o o . .
. o . . .
. . . o o
. . . . o
o o o . . # SI

. o . . .
. . . o .
. o o . .
. . o . o
o . o . . # NO
"""

def es_caso_base(problema):
    pass

def dividir(problema, x, y):
    pass

def combinar(s1,s2):
    pass

def mostrar(problema,x,y):
    print("----------")
    for i in range(len(problema)):
        for j in range(len(problema[i])):
            if i==x and j==y:
                print("*",end=" ")
            else:
                print(problema[i][j],end=" ")
        print("")


def resolver ( problema , x, y ):
    
    mostrar(problema,x,y)

    if problema[x][y] ==".":
        if x==4 and y==4:
            return True

        if y<4 and problema[x][y+1] ==".":# hacia la derecha
            s1 = resolver( problema, x, y+1)
            if s1:
                return True
        
        if x<4 and problema[x+1][y]==".": #hacia abajo
            s2 = resolver( problema, x+1, y)
            if s2:
                return True
        
        return False

  #subproblema1, subproblema2 = dividir ( problema , x, y )
  #solucion1 = resolver ( subproblema1 )
  #solucion2 = resolver ( subproblema2 )
  #return combinar ( solucion1 , solucion2 )

def test_walkable_path():

    caso1 = [
    [".","o","o",".","."],
    [".","o",".",".","."],
    [".",".",".","o","o"],
    [".",".",".",".","o"],
    ["o","o","o",".","."],
    ]

    caso2 = [
    [".","o",".",".","."],
    [".",".",".","o","."],
    [".","o","o",".","."],
    [".",".","o",".","o"],
    ["o",".","o",".","."],
    ]

    caso3 = [
    [".","o",".",".","."],
    [".",".",".","o","."],
    [".","o","o",".","."],
    [".",".","o",".","o"],
    ["o",".",".",".","."],
    ]

    #assert not resolver( caso2 , 0,0)
    #assert resolver(caso1, 0, 0)
    assert resolver(caso3, 0, 0)

test_walkable_path()