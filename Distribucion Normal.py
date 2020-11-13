from scipy import stats
import numpy as np

#print(stats.norm.__doc__)


#-----Ejemplo 6.2----------------------------------------------------
print("Ejemplo 6.2 **************************************")

#P(Z > 1.84)
normal = stats.norm(0,1) #Pasar con os parametros normalizados
a = 1-normal.cdf(1.84)
print("a:",a)
#Reciproca en vez de restarle al entero
a = normal.sf(1.84)
print("a:",a)
#P(-1.97 < Z < 0.86)
b = normal.cdf(0.86)-normal.cdf(-1.97)
print("b:",b)

#-----Ejemplo OTRO----------------------------------------------------
print("\nEjemplo OTRO **************************************")
#P(-1.68 < Z < 0)
a = normal.cdf(0)-normal.cdf(-1.68)
print("a:",a)
b = normal.cdf(2.73)-normal.cdf(.5)
print("b:",b)

#-----Ejemplo 6.4----------------------------------------------------
print("\nEjemplo 6.4 **************************************")

#P(45 < X < 62)
mu=50
sigma=10
normal = stats.norm(mu,sigma) #Pasar con os parametros normalizados
a = normal.cdf(62)-normal.cdf(45)
print("a:",a)

#-----Ejemplo 6.5----------------------------------------------------
print("\nEjemplo 6.5 **************************************")

#P(X > 340)
mu=300
sigma=50
normal = stats.norm(mu,sigma) #Pasar con os parametros normalizados
a = normal.sf(340)
print("a:",a)

#-----Ejemplo 6.6----------------------------------------------------
print("\nEjemplo 6.6 **************************************")

normal = stats.norm(40,6)
a = normal.ppf(.45) #Es el inverso de cdf
print("a:",a)
b = normal.isf(.14) #Es el inverso de sf
print("b:",b)