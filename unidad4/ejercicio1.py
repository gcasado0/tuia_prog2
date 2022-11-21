"""
Ejercicio 1: Dado un número entero compuesto, que es producto de dos números primos, 
hacer un algoritmo de fuerza bruta que encuentre su factorización. 
Analice la cantidad operaciones que este algoritmo requiere.
"""

def es_primo(numero):
  for i in range(2,numero):
    if (numero % i == 0):
      return False
  return True

def siguiente(intento_actual):  
  intento_actual+=1
  while intento_actual<x and not es_primo(intento_actual):
      intento_actual+=1
  return intento_actual

def es_solucion(intento_actual,x):
  if (x % intento_actual == 0):    
    return True


x = 5*7
intento_actual = 2 #primer numero primo

while intento_actual and not es_solucion(intento_actual,x):
  intento_actual = siguiente(intento_actual)
  print(intento_actual)

p2 = int(x/intento_actual)
if not es_primo(p2):
  print("Error el número ingresado no es correcto")
else:
  print(f"Resultado final: {x} = {intento_actual}*{p2}")