
from time import time
from random import shuffle
import sorting1
import sorting2
import sorting3
import matplotlib.pyplot as plt
import utils


# N y B a elección
N=30
B=100

tiempos1 = []
eficiencia1 = []
tiempos2 = []
eficiencia2 = []
tiempos3 = []
eficiencia3 = []
tiempos4 = []
eficiencia4 = []
cantidad = []
qs = sorting2.Ordenar()

for i in range(1,N):
  lista = list(range(B * i))
  cantidad.append(len(lista))
  shuffle(lista)
  print(len(lista))


  inicial = time()
  s1= sorting1.insertionSortShift(lista, eficiencia1)
  final = time()
  tiempos1.append(final - inicial)
  assert utils.esta_ordenada(s1)
  print("t1",final - inicial)

  qs.reset()
  inicial = time()
  s2 = qs.quickSort(lista)
  final = time()
  tiempos2.append(final - inicial)  
  eficiencia2.append(qs.comparaciones)
  assert utils.esta_ordenada(s2)
  print("t2",final - inicial)

  inicial = time()
  s3, comparaciones =sorting3.selectionSort(lista)
  final = time()
  tiempos3.append(final - inicial)
  eficiencia3.append(comparaciones)
  assert utils.esta_ordenada(s3)
  print("t3",final - inicial)

  inicial = time()
  s4 =sorting1.insertionSort(lista, eficiencia4)
  final = time()
  tiempos4.append(final - inicial)
  assert utils.esta_ordenada(s4)
  print("t4",final - inicial)


#Mostrar grafico
COLOR_Rojo = "#FF5733" 
COLOR_Verde = "#DAF7A6"
COLOR_Azul = "#2196F3" 
COLOR_Amarillo = "#FFF59D" 

plt.subplot(2, 2, 1)
plt.plot(cantidad, tiempos3, color=COLOR_Rojo, label='selectionSort')
plt.plot(cantidad, tiempos1, color=COLOR_Verde, label='insertionSortShift')
plt.plot(cantidad, tiempos4, color=COLOR_Amarillo, label='insertionSort')
plt.plot(cantidad, tiempos2, color=COLOR_Azul, label='quickSort')
plt.legend()
plt.ylabel('Time elapsed')

plt.subplot(2, 2, 2)
plt.plot(cantidad, eficiencia3, color=COLOR_Rojo, label='selectionSort')
plt.plot(cantidad, eficiencia1, color=COLOR_Verde, label='insertionSortShift')
plt.plot(cantidad, eficiencia4, color=COLOR_Amarillo, label='insertionSort')
plt.plot(cantidad, eficiencia2, color=COLOR_Azul, label='quickSort')
plt.legend()
plt.ylabel('Comparisons')

plt.subplot(2, 2, 3)
plt.plot(cantidad, tiempos2, color=COLOR_Azul, label='quickSort')
plt.legend()
plt.ylabel('Time elapsed')

plt.subplot(2, 2, 4)
plt.plot(cantidad, eficiencia2, color=COLOR_Azul, label='quickSort')
plt.legend()
plt.ylabel('Comparisons')
plt.show()