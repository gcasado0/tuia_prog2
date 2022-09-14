
class Stack():
  def __init__(self):
    self.lista = []

  def push(self, item):
    self.lista.append(item)

  def pop(self):
    return self.lista.pop()

  def isEmpty(self):
    return self.lista == []

class Calculadora(Stack):
    _operadores = ['+','-','*','/']

    def resolver(self, arg1, arg2, operador):
        if operador == '+':
            return arg1 + arg2
        elif operador == '-':
            return arg1 - arg2
        elif operador == '*':
            return arg1 * arg2
        elif operador == '/':
            return arg1 / arg2        

    def push(self, expresion):
        if expresion in self._operadores:
            arg2=self.pop()
            arg1=self.pop()
            resultado = self.resolver(arg1, arg2, expresion)
            super().push(resultado)
        else:
            super().push(expresion)
        

pila = Calculadora()
pila.push(1)
pila.push(2)
pila.push('+')
pila.push(3)
pila.push(4)
pila.push('-')
pila.push('*')
pila.push(5)
pila.push('+')
print("Calculo:", pila.pop())


"""
def calcular(pila):
    if len(pila.lista)==3:
        return pila.pop()
    else:
        pila2 = Stack()
        while not pila.isEmpty():
            valor = pila.pop()
            if valor in operadores:
                pila2.push(valor)
            else:
                arg1 = valor
                arg2 = pila.pop()
                operador = pila2.pop()
                parcial = resolver(arg1, arg2, operador)
                pila2.push(parcial)
        calcular(pila2)
"""




