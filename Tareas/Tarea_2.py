#ESTADISTICA INFERENCIAL / TAREA 1


import numpy as np
from scipy import stats

#help(stats.binom)
#.pmf = Densidad de Probabilidad
#.cdf = Acumulada de Probabilidad

#N = Tamaño de la población
#k = Numero de exitos
#n = Tamaño del muestreo
#x = Variable Aleatoria
"""
M = #Tamaño de la población
n = #Cantidad de los que hay del muestreo
N = #Tamaño del muestreo
k = #Numero de exitos
"""

print("********TAREA 2********")

#Ejercicio 5.29 ----------------------------------------
print("\nEJERCICIO 5.29 *************************************")
M = 9   #TOTAL
n = 4   #Narcisos en la muestra y se supone que lo demás sera tulipan
N = 6   #Muestra
hg1 = stats.hypergeom(M,n,N)
a = hg1.cdf(2)-hg1.cdf(1)
print("a:",a)

#Ejercicio 5.31 ----------------------------------------
print("\nEJERCICIO 5.31 *************************************")
print("Escribir la formula en el codigo directo en editor de latex")
#h(x;6,3,4)=\frac{\binom{4}{x}\binom{2}{3-x}}{\binom{6}{3}},X=1,2,3
M = 6   #Muetra
n = 4   #Cantidad de medicos
N = 3   #Elegidos al azar
hg = stats.hypergeom(M,n,N)
a = hg.cdf(3)-hg.cdf(1)
print("a:",a)

#Ejercicio 5.33 ----------------------------------------
print("\nEJERCICIO 5.33 *************************************")

M = 52   #Muestra
n = 12   #Cantidad de cartas con figuras
N = 7    #Elegidos al azar
hg = stats.hypergeom(M,n,N)
a = hg.cdf(2)-hg.cdf(1)
print("a:",a)

M = 52  #Muestra
n = 2   #Cartas que son reinas
N = 7   #Elegidos al azar
hg = stats.hypergeom(M,n,N)
b = hg.cdf(2)-hg.cdf(0)
print("b:",b)

#Ejercicio 5.35 ----------------------------------------
print("\nEJERCICIO 5.35 *************************************")

M = 50   #Muestra
n = M*.20   #Cantidad de defectuosos
N = 5   #Elegidos al azar
hg = stats.hypergeom(M,n,N)
a = hg.cdf(2)
print("a:",a)

#Ejercicio 5.36 ----------------------------------------
print("\nEJERCICIO 5.36 *************************************")
M = 25
n = 3   
N = 3  
hg = stats.hypergeom(M,n,N)
a = hg.cdf(0)
print("a:",a)

M = 25
n = 3   
N = 1  
hg = stats.hypergeom(M,n,N)
b = hg.cdf(1)-hg.cdf(0)
print("b:",b)

#Ejercicio 5.37 ----------------------------------------
print("\nEJERCICIO 5.37 *************************************")

n = 3
p = 3/25
bi = stats.binom(n,p)
a = bi.cdf(0)
print("a:",a)

n = 3
p = 1/25
bi = stats.binom(n,p)
b = bi.cdf(3)-bi.cdf(0)
print("b:",b)

#Ejercicio 5.39
print("\nEJERCICIO 5.39 *************************************")
n = 10
p = .5
bi = stats.binom(n,p)
a = 1-bi.cdf(2)
print("a:",a)

#Ejercicio 5.41
print("\nEJERCICIO 5.41 *************************************")
n = 18
p = 70/100
bi = stats.binom(n,p)
a = bi.cdf(13)-bi.cdf(9)
print("a:",a)

#Ejercicio 5.43
print("\nEJERCICIO 5.43 *************************************")
M = 12
N = 4  
hg = stats.hypergeom(M,2,N)
a = hg.cdf(1)-hg.cdf(0)
hg1 = stats.hypergeom(M,3,N)
a1 = hg.cdf(1)-hg1.cdf(0)
hg2 = stats.hypergeom(M,5,N)
a2 = hg.cdf(1)-hg2.cdf(0)
print("a:",a*a*a1*a2)
M = 12
N = 4  
hg = stats.hypergeom(M,2,N)
a = hg.cdf(2)-hg.cdf(0)
hg1 = stats.hypergeom(M,3,N)
a1 = hg.cdf(1)-hg1.cdf(0)
hg2 = stats.hypergeom(M,2,N)
a2 = hg.cdf(1)-hg1.cdf(0)
c=a*a1*a2
hg = stats.hypergeom(M,2,N)
a = hg.cdf(1)-hg.cdf(0)
hg1 = stats.hypergeom(M,3,N)
a1 = hg.cdf(2)-hg1.cdf(0)
hg2 = stats.hypergeom(M,2,N)
a2 = hg.cdf(1)-hg1.cdf(0)
c+=a*a1*a2
hg = stats.hypergeom(M,2,N)
a = hg.cdf(2)-hg.cdf(0)
hg1 = stats.hypergeom(M,3,N)
a1 = hg.cdf(1)-hg1.cdf(0)
hg2 = stats.hypergeom(M,2,N)
a2 = hg.cdf(1)-hg1.cdf(0)
c+=a*a1*a2
print("b:",c)

#Ejercicio 5.45
print("\nEJERCICIO 5.45 *************************************")
M = 25
n = 15  
N = 10 
hg = stats.hypergeom(M,n,N)
a = hg.cdf(5)-hg.cdf(4)
print("a:",a)

#Ejercicio 5.47
print("\nEJERCICIO 5.47 *************************************")
M = 20
n = 3  
N = 5 
hg = stats.hypergeom(M,n,N)
a = hg.cdf(0)
print("a:",a)
M = 20
n = 3  
N = 5 
hg = stats.hypergeom(M,n,N)
a = hg.cdf(2)-hg.cdf(1)
print("b:",a)
