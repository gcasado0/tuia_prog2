import itertools

def siguiente():
  if i<len(combinaciones):    
    return combinaciones[i]          
  return False

def es_solucion(intento_actual):  
  if sum(intento_actual)==magico:
    return True

magico = 6+7+3+10
lista = [3,6,7,8,9,10]
n = 4
i = 0
#combinaciones = [(a,b,c) for a in lista for b in lista for c in lista]
combinaciones = list(itertools.product(lista,repeat=n))

intento_actual = siguiente()
soluciones = []

while intento_actual:
  if es_solucion(intento_actual):
    soluciones.append(intento_actual)
  i+=1
  intento_actual = siguiente()


print(f"El numero mágico={magico} tiene como solución a:", soluciones)