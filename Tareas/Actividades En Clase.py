from scipy import stats
import numpy as np

#Actividades complementarias 03/11/20

#-----Ejemplo 6.7----------------------------------------------------
print("Ejemplo 6.7 **************************************")
normal = stats.norm(3,.5)
a = normal.cdf(2.3)
print("a:",a)

#-----Ejemplo 6.9----------------------------------------------------
print("\nEjemplo 6.9 **************************************")
normal = stats.norm(3,0.005)
a = normal.cdf(2.99)+(1-normal.cdf(3.01))
print("a:",a)

#-----Ejemplo 6.11----------------------------------------------------
print("\nEjemplo 6.11 **************************************")
normal = stats.norm(40,2)
a = 1-normal.cdf(43)
print("a:",a)