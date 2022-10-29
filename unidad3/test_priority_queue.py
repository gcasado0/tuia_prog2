class Queue():
  def __init__(self):
    self.lista = []

  def insert(self, elemento):
    n = len ( self.lista )
    j = n - 1
    while j >= 0:
      if elemento < self.lista[ j ]:
        j = j - 1
      else :
        break
    # Almacenamos el valor actual en el lugar que nos quedo disponible
    if j+1<n:
      self.lista.insert(j+1, elemento)
    else:
      self.lista.append(elemento)

  def remove(self):
    return self.lista.pop(0)
  
  def isEmpty(self):
    return self.lista == []

def test_priority_queue():
  cola = Queue()
  #test 1
  assert cola.isEmpty()
  cola.insert(1)
  cola.insert(3)
  cola.insert(2)
  assert not cola.isEmpty()
  assert cola.remove() == 1
  assert cola.remove() == 2
  assert cola.remove() == 3
  assert cola.isEmpty()
  #test 2
  cola.insert(8)
  cola.insert(6)
  cola.insert(-1)
  cola.insert(2)
  assert not cola.isEmpty()
  assert cola.remove() == -1
  assert cola.remove() == 2
  assert cola.remove() == 6
  assert cola.remove() == 8
  assert cola.isEmpty()

test_priority_queue()
