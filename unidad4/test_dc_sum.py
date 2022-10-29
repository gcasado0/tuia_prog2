

def es_caso_base(problema):
  if len(problema)==1:
    return True

def dividir(problema):
  mitad = len(problema)//2
  print(mitad)
  return problema[:mitad], problema[mitad:]

def combinar(s1,s2):
  return s1+s2

def resolver ( problema ):
  if es_caso_base ( problema ):
    return problema[0]

  subproblema1, subproblema2 = dividir ( problema )

  solucion1 = resolver ( subproblema1 )
  solucion2 = resolver ( subproblema2 )
  return combinar ( solucion1 , solucion2 )

problema = [5, 8, 7, 1, 3, 6]
s1 = resolver ( problema )
print (s1)

assert sum(problema) == s1
