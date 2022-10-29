
from test_creacion_tabla_hash import HashTable

class HashAbierto(HashTable):
    
    def insert(self, clave, elemento):
      hash = self.h(clave)
      if self.T[hash]: #colision
        for i in range(1, self.m):
          hash = (hash + i) % self.m
          if self.T[hash]== None:
            self.T[hash]= elemento
            return True
      else:
        self.T[hash]= elemento
        return True
      return False #sin lugar para insertar!
    
    def search(self, clave):
      hash = self.h(clave)
      i = 0
      while self.T[hash] and self.T[hash].clave != clave and i<self.m:
          i += 1
          hash = (hash + i) % self.m
      if self.T[hash] and self.T[hash].clave == clave:
        return self.T[hash]
      else:
        return False
      
class Cell():
  def __init__(self, clave, stock):
    self.clave = clave
    self.stock = stock

def test_hashing_abierto():

  def hashF(clave):
    return clave % 53 #numero primo > 50

  tabla = HashAbierto(53, hashF)
  tabla.insert(400, Cell(400,10))
  tabla.insert(200, Cell(200,20))
  tabla.insert(135, Cell(135,30))

  assert tabla.search(400).stock == 10
  assert tabla.search(200).stock == 20
  assert tabla.search(135).stock == 30
  assert not tabla.search(300)

test_hashing_abierto()
