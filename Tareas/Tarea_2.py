#ESTADISTICA INFERENCIAL / TAREA 1

import os
import numpy as np
from scipy import stats

#help(stats.binom)


#M = Tamaño de la población
#n = Numero de fracasos
#N = Tamaño del muestreo
#x = Numero de exitos

print("********TAREA 2********")

#Ejercicio 5.29 ----------------------------------------
print("\nEJERCICIO 5.29 *************************************")

M = 10
n = 2
N = 3
x = 0
hg = stats.hypergeom(M,n,N)

#a
a = hg.pmf(x)
print(a)