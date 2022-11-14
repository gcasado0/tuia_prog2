
from time import time
from random import shuffle
import sorting1
import sorting2
import matplotlib.pyplot as plt


# N y B a elección
N=100
B=100

tiempos1 = []
tiempos2 = []
cantidad = []
for i in range(N):
  lista = list(range(B * i))
  cantidad.append(len(lista))
  shuffle(lista)
  print(len(lista))

  inicial = time()
  s1=sorting1.insertionsort(lista)
  final = time()
  tiempos1.append(final - inicial)
  print("t1",final - inicial)

  inicial = time()
  s2=sorting2.quicksortmia(lista)
  final = time()
  tiempos2.append(final - inicial)
  print("t2",final - inicial)

#Mostrar grafico
COLOR_Verde = "#69b3a2" #Verde
COLOR_Azul = "#3399e6" #Azul

"""
fig, ax1 = plt.subplots(figsize=(15, 6))
ax2 = ax1.twinx()
ax1.plot(cantidad, tiempos1, color=COLOR_Verde)
ax2.plot(cantidad, tiempos2, color=COLOR_Azul)
plt.show()
"""

plt.figure(figsize = (15,6))
#plt.xticks(rotation = 90, fontsize=15);
#plt.yticks(fontsize=20);
#plt.xlabel(etiqueta_eje_x,fontsize=10)
#plt.ylabel(etiqueta_eje_y,fontsize=15)
#plt.title(titulo,fontsize=20);
#plt.savefig('imagen.png', bbox_inches = 'tight')

plt.plot(cantidad, tiempos1, color=COLOR_Verde)
plt.plot(cantidad, tiempos2, color=COLOR_Azul)

plt.show()



