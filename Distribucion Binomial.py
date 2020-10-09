# -*- coding: utf-8 -*-
from scipy import stats

#help(stats.binom)

#EJERCICIO 5.1 ---------------------------------------------------
n = 4
p = 3/4
bi = stats.binom(n,p)

print("Ejercicio 5.1--------------------")
#a
a = bi.cdf(2)-bi.cdf(1)
print(a)

#EJERCICIO 5.2 ---------------------------------------------------
print("\nEjercicio 5.2--------------------")
#Declarando objeto de tipo binomial
n=15
p=0.4
bi_1 = stats.binom(n,p)

#a P (X ≥ 10)
a = 1-(bi_1.cdf(9))
print (a)

#b P (3 ≤ X ≤ 8)
b = bi_1.cdf(8)-bi_1.cdf(2)
print (b)

#c P (X = 5 )
c = bi_1.cdf(5)-bi_1.cdf(4)
print (c)

#EJERCICIO 5.3 ---------------------------------------------------
print("\nEjercicio 5.3 ------------------")
#Declarando objeto de tipo binomial
n=20
p= 3/100
bi_2 = stats.binom(n,p)

#a P (X ≥ 1)
a = 1-bi_2.cdf(0)
print (a)

#b P (Y = 3)
n =10
p = a
bi_3 = stats.binom(n,p)

b = bi_3.cdf(3)-bi_3.cdf(2)
print (b)

#EJERCICIO 5.4 ---------------------------------------------------
print("\nEjercicio 5.4 ------------------")
#Declarando objeto de tipo binomial
n=10
p= 30/100
bi_4 = stats.binom(n,p)

#a P (X = 3)
a = bi_4.cdf(3)-bi_4.cdf(2)
print (a)

#b
b = 1-bi_4.cdf(3)
print(b)

#EJERCICIO 5.5 ---------------------------------------------------
print("\nEjercicio 5.5 ------------------")
#Declarando objeto de tipo binomial
n=15
p=.4
media = n*p
varianza = n*p*(1-p)
desviacion = varianza**(1/2)
print("Media: ",media)
print("Varianza: ",varianza)
print("Desviacion: ",desviacion)

#EJERCICIO 5.6 ---------------------------------------------------
print("\nEjercicio 5.6 ------------------")
#Declarando objeto de tipo binomial
n=10
p= 30/100
bi_5 = stats.binom(n,p)

#a
a = 1-bi_5.cdf(5)
print (a)






