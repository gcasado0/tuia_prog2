
print("++++++++++++++++ 2. Pila (Stack) ++++++++++++++++++")

"""
Las operaciones de lista que proporciona Python son similares a las operaciones que definen a una pila.
La interfaz no es exactamente la misma pero podemos escribir código para traducir del TDA pila a las
operaciones integradas (built-in) de listas en Python. Este código se denomina implementación del TAD
pila. En general, una implementación es un conjunto de métodos que satisfacen los requisitos sintácticos y
semánticos de una interfaz.
"""

class Stack:
    def __init__(self):
        self . items = []
    
    def push(self, item):
        self . items . append(item)
    
    def pop(self):
        return self . items .pop()
    
    def isEmpty(self):
        return (self . items == [])


pila = Stack()
pila.push(1)
print(pila.pop())
print(pila.isEmpty())


print("++++++++++++++++ 3. Colas (Queues) ++++++++++++++++++")

"""
El TDA Cola y el TDA Cola de Prioridad tienen el mismo conjunto de operaciones. La diferencia
está en la semántica de las operaciones: una cola usa la política FIFO; y una cola de prioridad (como
sugiere el nombre) utiliza la política de cola de prioridad.
"""

"""
3.1. El TDA Cola
El TDA cola se define mediante las siguientes operaciones:
__init__: inicializa una nueva cola vacía.
insert: agrega un nuevo elemento a la cola.
remove: eliminar y devolver un elemento de la cola. El artículo que se devuelve es el primero que se agregó.
isEmpty: Comprueba si la cola está vacía.
"""

print("++++++++++++++++ 3.2. Clase Nodo (Node) ++++++++++++++++++")

class Node :
    def __init__ (self , cargo =None , next = None ):
        self . cargo = cargo
        self . next = next

    def __str__ ( self ):
        return str( self . cargo )
    
    def printList ( self ):
        nodo = self
        while nodo :
            print(nodo)
            nodo = nodo . next


nodo1 = Node("1")
nodo2 = Node("2")
nodo3 = Node("3")
nodo1.next = nodo2
nodo2.next = nodo3

print(nodo1, nodo2, nodo3)
nodo1.printList()
nodo2.printList()

print("++++++++++++++++ 3.3. Cola Enlazada ++++++++++++++++++")
"""
La primera implementación del TDA Cola que veremos se llama Cola Enlazada porque está formado por
objetos Nodos Enlazados, que acabamos de introducir.
"""

class Queue :
    def __init__ ( self ):
        self . length = 0
        self . head = None

    def isEmpty ( self ):
        return ( self . length == 0)

    def insert (self , cargo ):
        node = Node ( cargo )
        node . next = None
        if self . head == None :
            # if list is empty the new node goes first
            self . head = node
        else :
            # find the last node in the list
            last = self . head
            while last . next :
                last = last . next
            # append the new node
            last . next = node
            self . length = self . length + 1 

    def remove ( self ):
        cargo = self . head . cargo
        self . head = self . head . next
        self . length = self . length - 1
        return cargo       
    
    def printList ( self ):
        nodo = self.head
        while nodo :
            print(nodo)
            nodo = nodo . next

cola = Queue()
cola.insert("test1")
cola.insert("test2")
print(cola.remove())


print("++++++++++++++++ 3.5. Cola Enlazada Mejorada ++++++++++++++++++")
"""
Nos gustaría una implementación del TDA Cola que pueda realizar todas las operaciones en tiempo constante.
Una forma de hacerlo es modificar la clase Queue para que mantenga una referencia tanto al primer como al
último nodo
"""
class ImprovedQueue :
    def __init__ ( self ):
        self . length = 0
        self . head = None
        self . last = None

    def isEmpty ( self ):
        return ( self . length == 0)

    def insert (self , cargo ):
        node = Node ( cargo )
        node . next = None
        if self . head == None :
            # if list is empty the new node goes first
            self.head = node
            self.last = node
        else :
            # find the last node in the list
            self.last.next = node
            self.last = node 
            self.length += 1
    
    def remove ( self ):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo 
    
    def printList ( self ):
        print("[",end='')
        nodo = self.head
        while nodo :
            print(nodo,end='->')
            nodo = nodo . next
        print("]")


icola = ImprovedQueue()
icola.insert("test1")
icola.insert("test2")
icola.insert("test3")
icola.printList()
print("remove:",icola.remove())
print("remove:",icola.remove())
print("remove:",icola.remove())
icola.printList()

print("++++++++++++++++ 3.6. Cola de Prioridad ++++++++++++++++++")
"""
El TDA Cola de Prioridad (Priority Queue) tiene la misma interfaz que el TDA Cola (Queue), pero
diferente semántica. De nuevo, la interfaz es:
__init__: inicializa una nueva cola vacía.
insert: agrega un nuevo elemento a la cola.
remove: eliminar y devolver un elemento de la cola. El artículo que se devuelve es el que tiene mayor
prioridad.
isEmpty: Comprueba si la cola está vacía.
"""

class PriorityQueue :
    def __init__ ( self ):
        self . items = []
    
    def isEmpty ( self ):
        return self . items == []

    def insert (self , item ):
        self . items . append ( item )

    def remove(self):
        i_maximo = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[i_maximo]:
                i_maximo=i
        return self.items.pop(i_maximo)

pcola = PriorityQueue()

pcola.insert(5)
pcola.insert(7)
pcola.insert(3)
pcola.insert(10)
while not pcola.isEmpty(): print(pcola.remove())