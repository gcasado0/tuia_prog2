
from test_creacion_tabla_hash import HashTable

class HashDirecto(HashTable):
    
    def insert(self, clave, elemento):
      hash = self.h(clave)
      self.T[hash]= elemento
    
    def search(self, clave):
      hash = self.h(clave)
      return self.T[hash]


def test_hashing_directo():

  def hashF(clave):
    return clave

  tabla = HashDirecto(1000, hashF)
  tabla.insert(400, 10)
  tabla.insert(200, 20)

  assert tabla.search(400) == 10
  assert tabla.search(200) == 20

test_hashing_directo
