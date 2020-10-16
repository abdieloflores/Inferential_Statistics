import numpy as np
from scipy import stats

#help(stats.hypergeom)

#.pmf = Densidad de Probabilidad
#.cdf = Acumulada de Probabilidad
"""
M = #Tamaño de la población
n = #Numero de fracasos
N = #Tamaño del muestreo
x = #Numero de exitos"""

#EJERCICIO 5.8 ---------------------------------------------------
print("Ejercicio 5.8--------------------")

M = 10
n = 2
N = 3
x = 0
hg = stats.hypergeom(M,n,N)

#a
a = hg.pmf(x)
print(a)

#EJERCICIO 5.9 ---------------------------------------------------
print("\nEjercicio 5.9--------------------")

M = 40 #Tamaño de la población
n = 3 #Numero de fracasos
N = 5 #Tamaño del muestreo
x = 1 #Numero de exitos
hg1 = stats.hypergeom(M,n,N)

a = hg1.pmf(x)
print(a)

#Media
media = ((N*n)/M)
print("Media:",media)
#Varianza
varianza = ((M-N)/(M-1))*N*(n/M)*(1-(n/M))
print("Varianza: ",varianza)
#Desviacion
desviacion = varianza**(1/2)
print("Desviacion Estandar: ",desviacion)
#Chebyshev para interpretar el intervalo μ ± 2σ.
k = 2
print("μ ± 2σ =  -",media-(k*desviacion),"  +",media+(k*desviacion))
#Probabilidad del intervalo
prob = 1-1/k**2
print("Probabilidad del intervalo: ",prob)


#EJERCICIO 5.10 ---------------------------------------------------
print("\nEjercicio 5.10--------------------")
M = 100
n = 12
N = 10
x = 3
hg2 = stats.hypergeom(M,n,N)

a = hg2.pmf(x)
print(a)

#Media
media = ((N*n)/M)
print("Media:",media)
#Varianza
varianza = ((M-N)/(M-1))*N*(n/M)*(1-(n/M))
print("Varianza: ",varianza)

#EJERCICIO 5.30 ---------------------------------------------------

#Resolviendo buscando drogas
print("\nEjercicio 5.30--------------------")
M = 15 #Tamaño de la población
n = 6 #Numero de fracasos
N = 3 #Tamaño del muestreo
x = 0 #A testear para eviar hacer 3 calculos de las probabilidades
hg1 = stats.hypergeom(M,n,N)

a = 1- hg1.pmf(x) #En vez de testear en 1, 2 y 3, solo muestreamos en 0 y lo quitamos a 1

print(a)
#Resolviendo buscando vitamians
print("Resolviendo buscando Vitaminas--------------------")
M = 15 #Tamaño de la población
n = 9 #Numero de fracasos
N = 3 #Tamaño del muestreo
x = 3 #A testear para eviar hacer 3 calculos de las probabilidades
hg1 = stats.hypergeom(M,n,N)

a = 1- hg1.pmf(x) #En vez de testear en 1, 2 y 3, solo muestreamos en 0 y lo quitamos a 1

print(a)
