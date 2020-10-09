# -*- coding: utf-8 -*-
import numpy as np
from scipy import stats

help(stats.multinomial)

#EJERCICIO 5.7 ---------------------------------------------------
print("Ejercicio 5.7--------------------")
x = [2,1,3] #Ordenamiento
p = 6 #Cantidad
n = [2/9,1/6,11/18] #Probabilidades
rv = stats.multinomial(p,n)

#a
a = rv.pmf(x)
print(a)