
## traer codigo para crear un arbol binario
# Un árbol binario completo es un árbol binario en el que cada vértice tiene dos o cero hijos.

class BinaryTree:
  def __init__ ( self , cargo , left = None , right = None ):
    self . cargo = cargo
    self . left = left
    self . right = right
  
  def __str__ ( self ):
    return str ( self . cargo )

def printTreeInOrder(tree, nivel):
  if tree == None:
    return
  printTreeInOrder(tree.left, nivel+1)
  print("-" * nivel + ">", end="") 
  print(tree.cargo)
  printTreeInOrder(tree.right, nivel+1)

def es_solucion (candidatos):
  return candidatos==[None, None]

def elegir_candidato(hijos):  
  return hijos[0] if hijos[0].cargo>hijos[1].cargo else hijos[1]

def es_factible (eleccion):
  return True

def largest_sum_path(tree):
  candidatos = [tree.left, tree.right]
  eleccion_actual = [tree]

  while not es_solucion(candidatos):
    x = elegir_candidato(candidatos)
    if es_factible( eleccion_actual + [x]):
      eleccion_actual.append(x)
    candidatos = [x.left, x.right]

  return eleccion_actual

def test_largest_sum_path():

  tree1 = BinaryTree (3 , BinaryTree (5) , BinaryTree (8))
  tree2 = BinaryTree (4 , BinaryTree (6) , BinaryTree (7))
  tree3 = BinaryTree (1 , tree1 , tree2)

  printTreeInOrder(tree3,0)
  s1=largest_sum_path(tree3)
  for x in s1:
    print(x)

test_largest_sum_path()


