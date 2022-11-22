
def esta_ordenada(lista):
  for i in range(len(lista)-1):
    if lista[i]>lista[i+1]:
      return False
  return True

from time import time
def medir(f):
  def fmedida(x):
    inicio = time()
    retorno = f(x)
    fin = time()
    print("Elapsed time: {:0.6f}".format(fin-inicio))
    return retorno
  return fmedida

import random
def listaAleatorios(n):
  lista = [0]  * n
  for i in range(n):
      lista[i] = random.randint(0, 1000)
  return lista  


