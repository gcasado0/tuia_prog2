import random

class Carta():
  _apodos = {1:"As", 10:"Sota", 11:"Caballo", 12:"Rey"}

  def __init__(self, palo=None, numero=None, es_comodin=False) -> None:
    self.palo = palo
    self.numero = numero
    self.es_comodin = es_comodin

  def __str__(self) -> str:
    if self.es_comodin:
      return "Comodín"
    else:
      if self.numero in self._apodos.keys():
        salida = self._apodos[self.numero]
      else:
        salida = str(self.numero)
      return f"{salida} de {self.palo}"
    
  def __eq__(self, other):
     return self.es_comodin == other.es_comodin and \
           self.numero == other.numero and \
           self.palo == other.palo
    

def test_carta():
  ancho = Carta("espadas",1)
  assert ancho.numero == 1
  assert ancho.palo == "espadas"
  assert ancho.es_comodin == False

  comodin = Carta(es_comodin=True)
  assert comodin.es_comodin == True
  assert comodin.palo == None
  assert comodin.numero == None

def test_str():
  ancho = Carta("espadas",1)
  comodin = Carta(es_comodin=True)
  rey = Carta("espadas", 12)
  assert str(ancho) == "As de espadas"
  assert str(comodin) == "Comodín"
  assert str(rey) == "Rey de espadas"

def test_igual():
  rey1 = Carta("espadas", 12)
  rey2 = Carta("espadas", 12)
  assert rey1 == rey2
  comodin = Carta(es_comodin=True)
  assert rey1 != comodin


class Mazo():
    def __init__(self) -> None:
        self.mazo = []
        comodin = Carta(es_comodin=True)
        self.mazo.append(comodin)
        self.mazo.append(comodin)
        self.palos = ["Espadas", "Copas", "Bastos", "Oros"]
        for palo in self.palos:
            for numero in range(1,13):
                carta = Carta(palo,numero)
                self.mazo.append(carta)

    def cantidad(self):
        return len(self.mazo)

    def mezclar(self):
        longitud = self.cantidad()
        for i in range(0,longitud):
            posicion = random.randrange(longitud)
            carta = self.mazo.pop(posicion)
            self.mazo.insert(0,carta)
    
    def mostrar(self):
        print("***************************")
        for c in self.mazo:
            print(c)
        print(" --- Longitud: "+str(self.cantidad())+" --- " )
        print("***************************")

    #Ejercicio 7: Implementar en la clase Mazo, un método que permita sacar una carta 
    # específica del mazo, y que devuelva True si la carta estaba presente o False si no lo estaba.
    def remover_carta(self, palo=None, numero=None, es_comodin=False):
      for c in self.mazo:
        if c.numero == numero and c.palo==palo and c.es_comodin==es_comodin:
          self.mazo.remove(c)
          return True
      return False

    #Ejercicio 8: Implementar un método sacar_carta para robar una carta del mazo, 
    # es decir, para sacar aquella que se encuentra primera.
    def sacar_carta(self):
      return self.mazo.pop(0)
    
    #Ejercicio 9: Implementar un método que nos permita saber si quedan cartas en el mazo
    def esta_vacio(self):
      return len(self.mazo) == 0

    #Ejercicio 12: Agregar al mazo un método para repartir cartas. 
    #El método deberia recibir una lista de manos, las cuales reciben las cartas, 
    # y la cantidad de cartas a repartir en cada mano.
    def repartir(self, manos, cantidad):
      for mano in manos:
        for i in range(cantidad):
          mano.agregar(self.sacar_carta())


def test_init():
  mazo = Mazo()
  assert mazo.cantidad() == 50
  assert mazo.esta_vacio() == False

def test_operaciones():
  mazo = Mazo()
  assert mazo.remover_carta("Espadas",1) == True
  assert mazo.remover_carta("Espadas",1) == False
  mazo.mezclar()
  carta = mazo.sacar_carta()
  if carta.es_comodin:
    assert mazo.remover_carta(carta.palo ,carta.numero, carta.es_comodin) == True
  else:
    assert mazo.remover_carta(carta.palo ,carta.numero, carta.es_comodin) == False

#Ejercicio 10 Escribir una clase Mano, que represente la mano de un jugador 
# en algun juego de cartas. 
# Tener en cuenta que necesitaremos los métodos sacar_carta y otros ya definidos en Mazo. 
# Además, necesitaremos asociar el nombre del jugador que tiene esta mano
class Mano():
  def __init__(self, jugador) -> None:
     self.jugador = jugador
     self.mano = []
  
  #Ejercicio 11: Necesitaremos que una mano tenga funcionalidad para agregar cartas a la mano 
  # y sacar cartas de la mano. 
  # ¿Cuantos métodos debemos definir? Definir solamente aquellos métodos necesarios.

  def agregar(self, carta):
    self.mano.append(carta)
  
  def remover_carta(self, palo=None, numero=None, es_comodin=False):
      for c in self.mano:
        if c.numero == numero and c.palo==palo and c.es_comodin==es_comodin:
          self.mano.remove(c)
          return True
      return False
  
  #Ejercicio 13: Agregar funcionalidad para imprimir una mano, mostrando a quien pertenece 
  # y que cartas contiene
  def mostrar(self):
      print(f"**** Mano: {self.jugador} ****")
      for c in self.mano:
          print(c)
      print("***************************")


#Ejercicio 14: Agregar una clase Juego que represente un juego arbitrario con cartas españolas. 
# Recordar que un juego con cartas españolas siempre involucra un mazo que generalmente se mezcla.
class Juego():
  def __init__(self) -> None:
     self.mazo = Mazo()
     self.mazo.mezclar()

#Ejercicio 15: Heredar una clase TrucoArgentino que represente un juego de truco argentino 
# para dos jugadores. 
# Recordar:
# Antes de empezar a jugar se deben quitar los 8 y los 9 de todos los palos, y los dos comodines.
# se deben inicializar dos manos de tres cartas cada una. 
# Se reciben por parametros al constructor los nombres de ambos jugadores.

class TrucoArgentino(Juego):
    def __init__(self, jugador1, jugador2) -> None:
      super().__init__()
      #remover cartas
      self.mazo.remover_carta(es_comodin=True)
      self.mazo.remover_carta(es_comodin=True)
      for palo in self.mazo.palos:
        self.mazo.remover_carta(palo,8)
        self.mazo.remover_carta(palo,9)

      #inicializar manos
      self.mano1 = Mano(jugador1)
      self.mano2 = Mano(jugador2)
      manos = []
      manos.append(self.mano1)
      manos.append(self.mano2)
      self.mazo.repartir(manos,3)

    def mostrar(self):
      self.mazo.mostrar()
      self.mano1.mostrar()
      self.mano2.mostrar()

    #Ejercicio 16: Implementar un método .gana_envido() que devuelva el nombre del jugador 
    # que tiene mas puntos de envido.
    # Asumimos que nuestros jugadores son muy malos en el truco y nunca mienten.
    # Jugamos sin flor.
    # Recordar que para calcular el envido, si un jugador posee dos o más cartas de igual palo, 
    # los puntos de envido equivale a la suma del puntaje de dos cartas del mismo palo elegidas 
    # por el jugador más veinte puntos (10, 11 y 12 no suman). 
    # Jugamos asumiendo que mano1 es mano del partido (es decir, gana el envido en caso de empate).

    def _sumar_puntos_flor(self,mano):
      acumulador = {}
      cantidad = {}
      for carta in mano.mano:
        if carta.numero < 10:
          if carta.palo in acumulador:
            acumulador[carta.palo] += carta.numero
            cantidad[carta.palo] +=1
          else:
            acumulador[carta.palo] = carta.numero
            cantidad[carta.palo] = 1
      maximo = 0
      for palo, cant in cantidad.items():
          if cant>1:
              return acumulador[palo] + 20
          else:
            if acumulador[palo]>maximo:
              maximo = acumulador[palo]
      return maximo

    def _sumar_puntos(self,mano):
      #descarto cartas superiores o iguales a 10
      cartas_validas = []
      for c in mano.mano:
          if c.numero >= 10:
            cartas_validas.append(Carta(c.palo,0))
          else:
            cartas_validas.append(Carta(c.palo,c.numero))

      #analizo si hay convinacion de palos
      maximos = []
      if len(cartas_validas)==3:
          if cartas_validas[0].palo == cartas_validas[1].palo:
            maximos.append(cartas_validas[0].numero + cartas_validas[1].numero)
          if cartas_validas[0].palo == cartas_validas[2].palo:
            maximos.append(cartas_validas[0].numero + cartas_validas[2].numero)
          if cartas_validas[1].palo == cartas_validas[2].palo:
            maximos.append(cartas_validas[1].numero + cartas_validas[2].numero)
          if len(maximos):#si hay alguna convinacion
            return max(maximos)+20
      elif len(cartas_validas)==2:
          if cartas_validas[0].palo == cartas_validas[1].palo:
            return cartas_validas[0].numero + cartas_validas[1].numero + 20
      #no hay convinacion de palos
      maximo=0
      for c in cartas_validas:
          if c.numero>maximo:
            maximo=c.numero
      return maximo
          

    def gana_envido(self):
      puntos1 = self._sumar_puntos(self.mano1)
      puntos2 = self._sumar_puntos(self.mano2)
      print(puntos1)
      print(puntos2)

      if puntos1 >= puntos2:
        return self.mano1.jugador
      else:
        return self.mano2.jugador

def test_suma_puntos():
  truco = TrucoArgentino("Pedro", "Lucho")
  mano = Mano("j1")
  mano.agregar(Carta("Espadas",1))
  assert truco._sumar_puntos(mano) == 1
  mano.agregar(Carta("Espadas",7))
  assert truco._sumar_puntos(mano) == 28
  mano.agregar(Carta("Espadas",6))
  assert truco._sumar_puntos(mano) == 33
  mano2 = Mano("j2")
  mano2.agregar(Carta("Oros",1))
  mano2.agregar(Carta("Espadas",7))
  mano2.agregar(Carta("Bastos",6))
  assert truco._sumar_puntos(mano2) == 7
  mano3 = Mano("j3")
  mano3.agregar(Carta("Oros",11))
  mano3.agregar(Carta("Espadas",12))
  mano3.agregar(Carta("Bastos",10))
  assert truco._sumar_puntos(mano3) == 0
  
  

#----------------------------- MAIN -------------------------------

truco = TrucoArgentino("Pedro", "Lucho")
truco.mostrar()
jugador = truco.gana_envido()
print(jugador)
