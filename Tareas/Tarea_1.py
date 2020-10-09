#ESTADISTICA INFERENCIAL / TAREA 1

import os
import numpy as np
from scipy import stats

#help(stats.binom)

#Para binomial μ = np y σ^2 = npq.

# n = numero de pruebas
# p = probabilidad (exitos)
# q = 1-p (fracasos)
# x = donde va a ser evaluado

print("********TAREA 1********")

#Ejercicio 5.1 ----------------------------------------
print("\nEJERCICIO 5.1 *************************************")

print("La media es \mu = \frac{1}{k}\\sum_{i^1}^{k}x_{i}")
print("La varianza es \mu = \frac{1}{k}\sum_{i^1}^{k}\left ( x_{i}-\mu  \right )^{2}")

#Ejercicio 5.3 ----------------------------------------
print("\nEJERCICIO 5.3 *************************************")
"""De un equipo de 10 empleados, y mediante la selección
al azar de una etiqueta contenida en una caja
que contiene 10 etiquetas numeradas del 1 al 10, se elige
a uno para que supervise cierto proyecto. Calcule la
fórmula para la distribución de probabilidad de X que
represente el número en la etiqueta que se saca. ¿Cuál
es la probabilidad de que el número que se extrae
sea menor que 4?"""
n = 10
p = 1/10
bi1 = stats.binom(n,p)

resultado = bi1.cdf(3)
print(resultado)

#Ejercicio 5.5 ----------------------------------------
print("\nEJERCICIO 5.5 *************************************")
n = 20
p = 30/100
bi2 = stats.binom(n,p)

resultado = 1-bi2.cdf(9)
print("a:",resultado)
resultado = bi2.cdf(4)
print("b:",resultado)
resultado = bi2.cdf(5)-bi2.cdf(4)
print("c:",resultado)
print("Esta sobrado lo que se menciona.")


#Ejercicio 5.7
print("\nEJERCICIO 5.7 *************************************")
n = 10
p = 70/100
bi3 = stats.binom(n,p)

resultado = bi3.cdf(4)
print("a:",resultado)
bi3 = stats.binom(20,p)
resultado = bi3.cdf(9)
print("b:",resultado)

#Ejercicio 5.9
print("\nEJERCICIO 5.9 *************************************")
n = 15
p = 25/100
bi4 = stats.binom(n,p)

resultado = bi4.cdf(6)-bi4.cdf(2)
print("a:",resultado)
resultado = bi4.cdf(3)
print("b:",resultado)
resultado = 1-bi4.cdf(5)
print("b:",resultado)

#Ejercicio 5.11
print("\nEJERCICIO 5.11 *************************************")
n = 7
p = 0.9
bi5 = stats.binom(n,p)

resultado = bi5.cdf(5)-bi5.cdf(4)
print("a:",resultado)

#Ejercicio 5.13
print("\nEJERCICIO 5.13 *************************************")
n = 5
p = 70/100
bi6 = stats.binom(n,p)

resultado = 1-bi5.cdf(2)
print("a:",resultado)

#Ejercicio 5.15
print("\nEJERCICIO 5.15 *************************************")
n = 5
p = 60/100
bi6 = stats.binom(n,p)

resultado = bi6.cdf(0)
print("a:",resultado)
resultado = bi6.cdf(1)
print("b:",resultado)
resultado = 1-bi6.cdf(3)
print("c:",resultado)

#Ejercicio 5.17
print("\nEJERCICIO 5.17 *************************************")
"""Si X representa el número de personas del ejercicio
5.13 que creen que los antidepresivos no curan sino
que sólo disfrazan el problema real, calcule la media y
la varianza de X si se seleccionan al azar 5 personas."""
n = 5
p = 60/100
media = n*p
varianza = n*p*(1-p)
print("Media: ",media)
print("Varianza: ",varianza)

#Ejercicio 5.19
print("\nEJERCICIO 5.19 *************************************")
print("Revisar en clase----")

#Ejercicio 5.21
print("\nEJERCICIO 5.21 *************************************")
x = [0,0,2,1] #Ordenamiento
p = 7 #Cantidad
n = [.01,.10,.05,.02] #Probabilidades
rv = stats.multinomial(p,n)

a = rv.pmf(x)
print(a)

#Ejercicio 5.23
print("\nEJERCICIO 5.23 *************************************")
x = [3,3,1,2] #Ordenamiento
p = 9 #Cantidad
n = [.4,.2,.3,.1] #Probabilidades
rv = stats.multinomial(p,n)

a = rv.pmf(x)
print(a)

#Ejercicio 5.25
print("\nEJERCICIO 5.25 *************************************")
n = 20
p = .10
bi6 = stats.binom(n,p)

resultado = bi6.cdf(3)
print("a:",resultado)

#Ejercicio 5.27
print("\nEJERCICIO 5.25 *************************************")
n = 20
p = .9
bi6 = stats.binom(n,p)

resultado = bi6.cdf(18)-bi6.cdf(17)
print("a:",resultado)
resultado = 1-bi6.cdf(14)
print("b:",resultado)
bi6 = stats.binom(n,1-p)
resultado = 1-bi6.cdf(1)
print("c:",resultado)
