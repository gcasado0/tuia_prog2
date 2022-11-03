def insertar_en_orden(lista, elemento):
    """Dada una lista ordenada, devuelve una nueva lista con el elemento
    en la posicion correspondiente."""

    for i in range(len(lista)): # Recorremos la lista...
        if elemento < lista[i]: # ...buscando un lugar en el medio.
            return lista[:i] + [elemento] + lista[i:]

    return lista + [elemento]   # Si no lo encontramos, va al final.

class PriorityQueue:
    def __init__(self, lista = None):
        self.lista = lista if lista else []

    def insert(self, elemento):
        self.lista = insertar_en_orden(self.lista, elemento)

    def remove(self): # Mayor elemento => Mayor prioridad
        return self.lista.pop()

    def __str__(self):
        return f"{self.lista}"