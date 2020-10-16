# -*- coding: utf-8 -*-
"""
EXAMEN PRIMER PARCIAL "ESTADISTICA INFERENCIAL"
"""
from scipy import stats

#PROBLEMA 1 **********************************************
print("Problema 1 ------------------------\n")
n = 8
p = 60/100
bi = stats.binom(n,p)
a = bi.cdf(3)-bi.cdf(2)
print("   a:",a)

n = 8
p = 60/100
bi = stats.binom(n,p)
a = 1-bi.cdf(4)
print("   b:",a)

#PROBLEMA 2 **********************************************
print("\nProblema 2 ------------------------\n")
n = 8
p = 60/100
bi = stats.binom(n,p)
a = bi.cdf(6)-bi.cdf(5)
print("   a:",a)

#PROBLEMA 3 **********************************************
print("\nProblema 3 ------------------------\n")
M = 9   
n = 5
N = 4   
hg1 = stats.hypergeom(M,n,N)
a = hg1.cdf(2)-hg1.cdf(1)
print("   a:",a)

#PROBLEMA 4 **********************************************
print("\nProblema 4 ------------------------\n")
M = 50   
n = M*.20   
N = 5   
hg = stats.hypergeom(M,n,N)
a = hg.cdf(2)
print("   a:",a)

#PROBLEMA 5 **********************************************
print("\nProblema 5 ------------------------\n")
#La solucione con prueba y error cambiando x.
n = 20
p = 20/100
x=4
bi = stats.binom(n,p)
a = 1-bi.cdf(x)
print("   Con x =",x," da:",a)
print("   a:  4")

#La solucione con prueba y error cambiando y.
n = 20
p = 1-(20/100)
y=14
bi = stats.binom(n,p)
a = 1-bi.cdf(y)
print("   Con y =",y," da:",a)
print("   b:  14")

