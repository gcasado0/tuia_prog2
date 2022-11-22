"""
Ejercicio 4: ¿Es quicksort un algoritmo Divide & Conquer? Justifique
1) saber si estas en un caso base y resolver el caso base
2) saber como dividir el problemas en subproblemas independientes
3) saber como combinar las soluciones de los subproblemas para llegar a solucion final

"""
import utils

def es_caso_base(x):#extender caso base para que incluya hasta 2 elementos
    if len(x)<=1:
        return True
    return False

def resolver_caso_base(x):
    return x
    
def dividir(lista):
    def elegir_pivote(lista):
        return lista[0] #pivote a ciegas

    pivote = elegir_pivote(lista)
    menores = []
    mayores = []
    for x in lista:
        if x<pivote:
            menores.append(x)
        elif x>pivote:
            mayores.append(x)
    print(menores, pivote, mayores)
    return menores, pivote, mayores

def combinar(s1,pivote,s2):
    return s1+[pivote]+s2


def resolver(problema):
    if es_caso_base(problema):
        return resolver_caso_base(problema)

    p1, pivote, p2 = dividir(problema)
    s1 = resolver(p1)
    s2 = resolver(p2)

    return combinar(s1,pivote,s2)

lista = utils.listaAleatorios(10)

s1 = resolver(lista)

print(lista)
print(s1)
assert utils.esta_ordenada(s1)



