
from utils import esta_ordenada

def elegir_pivote ( A ):
    # Tecnica de elección a ciegas, elegimos siempre el
    # primer elemento de la sublista a ordenar
    return A[0]

def comparar(x,y):
  if x<y:
    return -1
  elif x>y:
    return 1
  else:
    return 0

def quicksort (A , c):
  if len ( A ) < 2:
    # Caso base : listas trivialmente ordenadas
    return A
  
  # Elegimos un pivote
  pivote = elegir_pivote ( A )
  # Usamos listas por comprensión para
  # obtener las sublistas que debemos ordenar
  
  menores = [ x for x in A if c(x,pivote)==-1 ]
  mayores = [ x for x in A if c(x,pivote)==1 ]

  # Llamamos recursivamente a cada lado
  menores_ordenados = quicksort(menores, c)
  mayores_ordenados = quicksort(mayores, c)
  # Construimos la respuesta
  return menores_ordenados + [ pivote ] + mayores_ordenados

def test_higher_order_quicksort():
  lista=[1,3,2,6,8,5,12]
  assert not esta_ordenada(lista)

  s1 = quicksort(lista, comparar)
  print(s1)
  assert esta_ordenada(s1)


if __name__ == "__main__":
  test_higher_order_quicksort()
