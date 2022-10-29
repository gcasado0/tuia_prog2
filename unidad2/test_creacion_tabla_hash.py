
class HashTable():
  def __init__ ( self , capacity , hashFunction ):
    self.m = capacity
    self.h = hashFunction
    self.T = [ None ] * self.m
  


def hash(clave):
  return clave

def test_creacion_tabla_hash():
  t1 = HashTable(10, hash)

  assert len(t1.T)==10
    
  
