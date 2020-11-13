from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


#help(stats.uniform)

"""
Definicion es stats.uniform(A,B-A)
    A = Limite Inferior
    B = Limite Superior
    B-A = Rango
"""


#Ejercicio 6.1
print("\nEjercicio 6.1")
    
uni = stats.uniform(0,4-0)
a=uni.cdf(3)
print(a)

#Graficando
"""
x = np.linspace(0,4,101)
plt.plot(x,uni.pdf(x),'-r')
plt.grid(True)
plt.ylim(0,1)
plt.xlim(0.5)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x;0,4)$')
plt.show()
"""

#Ejercicio 6.2
print("\nEjercicio 6.2")
    
uni = stats.uniform(1,5-1)
a = uni.cdf(4)-uni.cdf(2.5)
print("a:",a)   

#Ejercicio 6.3
print("\nEjercicio 6.3")
    
uni = stats.uniform(7,10-7)
a = uni.cdf(8.8)
print("a:",a)
b = uni.cdf(9.5)-uni.cdf(7.4)
print("b:",b)
c = uni.cdf(10)-uni.cdf(8.5)
print("c:",c)

#Ejercicio 6.4
print("\nEjercicio 6.4")
    
uni = stats.uniform(0,10-0)
a = 1-uni.cdf(7)
print("a:",a)
b = uni.cdf(7)-uni.cdf(2)
print("b:",b)