print("++++++++++++++++ 4.1. Definición de clases propias ++++++++++++++++++")
class Vacia :
    """ esta clase no hace nada !"""
    pass

x = Vacia ()
print (x)

y = Vacia ()
print (y)

print(x is y)
z = x
print(z is x)
print(z)

print ( Vacia )
print ( isinstance (Vacia , type ))
print ( isinstance (5 , int ))


print("++++++++++++++++ 5. Herencia Simple ++++++++++++++++++")
class Pet:
    _number_of_legs = 4 #atributo de clase

    def __init__ (self , name , weight , owner , sex , hair_color):
        self.name = name #atributo de instancia
        self.weight = weight
        self.owner = owner
        self.sex = sex
        self.hair_color = hair_color
    
    def play (self , toy ):
        print (f"{ self . name } is playing with {toy }!")

    def eat( self ):
        print (f"{ self . name } is eating ")
        self . weight += 0.1

    def __str__ ( self ):
        return f"Soy { self . name } y mi dueña es { self . owner }"



class Cat( Pet ):
    def __init__ (self , character , *args, **kwargs ):
        super (). __init__ (*args , **kwargs )
        self.character = character

    def meow ( self ):
        print (f"{ self . name } says 'meow'")

class Dog(Pet):
    def woof ( self ):
        print (f"{ self . name } says 'woof '")
    #override
    def eat( self ):
        print (f"{ self . name } is eating !")
        self.weight += 0.2

melon = Cat("friendly", "Melon",6,"Sofi","Macho", ["blanco","naranja"],)

amelia = Cat("not friendly",
"Amelia",4,"Pauli","Hembra",
["negro","marron","blanco"],
)

bobo = Cat("very bad","Bobo",5,"Mela","Macho",["Gris"])

leon = Dog("León", 26, " Romi ", " Macho ", [" Marron "])

print(melon)
amelia.meow()
bobo.play("pelota")
print(f"legs of Amelia: {amelia._number_of_legs}")
leon.woof()

bobo.eat()
leon.eat()
print (f" Despues de comer , bobo pesa : { bobo.weight }")
# Despues de comer , bobo pesa 5.1
print (f" Despues de comer , leon pesa : { leon.weight }")
# Despues de comer , leon pesa 26.2

print ( bobo . character ) # friendly
print ( bobo . name ) # Bobo

print("isinstance (bobo , Cat) =",isinstance (bobo , Cat))
print("isinstance (bobo , Pet) =",isinstance (bobo , Pet))
print("isinstance (bobo , Dog) =",isinstance (bobo , Dog))
print("isinstance (bobo , object) =",isinstance (bobo , object))
