from importlib.resources import Package


from time import time

def medir(f):
  def fmedida(x,y):
    inicio = time()
    retorno = f(x,y)
    fin = time()
    print(fin-inicio)
    return retorno
  return fmedida

def esta_ordenada(lista):
  for i in range(len(lista)-1):
      if lista[i]>lista[i+1]:
          return False
  return True