"""
Tenemos una mochila con capacidad M = 5kg
y los siguientes objetos, queremos elegir que objetos llevar de forma de
maximizar el valor de lo que llevamos, pero sin exceder el peso maximo.
Objeto (i) Valor (vi) Peso (ci)
objeto 1 10usd 1 kg
objeto 2 20usd 3 kg
objeto 3 15usd 2 kg
objeto 4 20usd 4 kg
"""


print("Resuelva con un algoritmo voraz")

def rendimiento(objeto):
    return objeto[0]/objeto[1] #valor por kilo

def elegir_candidato():
    #mayor valor y menor peso
    maximo = 0
    for x in candidatos:
        if rendimiento(x)>maximo:
            maximo = rendimiento(x)
            candidato = x
    print("candidato", candidato)
    return candidato

def es_factible(eleccion):
    total = 0
    for x in eleccion:
        total += x[1]
    if total<=5:
        return True
    else:
        return False


def es_solucion(eleccion):
    if candidatos == []:
        return True

candidatos = [(10,1), (20,3), (15,2), (20,4)]

print(candidatos)
eleccion_actual = []

while not es_solucion(eleccion_actual):
    x = elegir_candidato()
    candidatos.remove(x)
    if es_factible(eleccion_actual+[x]):
        eleccion_actual.append(x)
    
print(eleccion_actual)

""""
(b) Resuelva con un algoritmo de fuerza bruta. 
Tenga en cuenta que necesitaran hacer una modificacion a la estructura general para quedarse
con la mejor solucion.
"""

print("Resuelva con un algoritmo de fuerza bruta")


def es_solucion_bruta(eleccion):
    total = 0
    for x in eleccion:
        total += x[1]
    if total<=5:
        return True
    else:
        return False

def siguiente(i):    
    combinacion = []
    if i<len(posibilidades):
        posibilidad = posibilidades[i]
        for j, agregar in enumerate(posibilidad):
            if agregar:
                combinacion.append(candidatos[j])        
    return combinacion

i = 1
posibilidades = [[s,x,y,z] for s in [0,1] for x in [0,1] for y in [0,1] for z in [0,1]]
candidatos = [(10,1), (20,3), (15,2), (20,4)]
intento_actual = siguiente(i)
soluciones = []
maximo=0
max_solucion = None
while intento_actual:
    if es_solucion_bruta(intento_actual):
        soluciones.append(intento_actual)
        total = sum([valor for valor, peso in intento_actual])
        print("solucion", intento_actual," total:", total)
        if total>maximo:
            maximo = total
            max_solucion = intento_actual

    i=i+1
    intento_actual = siguiente(i)


print("Solucion optima: ",max_solucion)


