from scipy import stats

#Ejercicio 6.15 ****************************************
print("\nEjercicio 6.15 -------------------")
normal = stats.norm(24,3.8)

a = normal.sf(30)
print("a)",a)
b = normal.sf(15)
print("b)",b)
c = normal.sf(25)
print("c)",c)
d = normal.isf(.25)
print("d)",d)
n = 3
p = a
bi = stats.binom(n,p)
e = bi.cdf(2)-bi.cdf(1)
print("e)",e) 

#Ejercicio 6.16 ****************************************
print("\nEjercicio 6.16 -------------------")
normal = stats.norm(99.61,0.08)

a = normal.cdf(99.7)-normal.cdf(99.5)
print("a)",a)
b = normal.isf(0.05)
print("b)",b)

#Ejercicio 6.17 ****************************************
print("\nEjercicio 6.17 -------------------")
normal = stats.norm(10,2)

a = normal.ppf(0.03)
print("a)",a)

#Ejercicio 6.18 ****************************************
print("\nEjercicio 6.18 -------------------")
normal = stats.norm(174.5,6.9)

a = normal.cdf(159.75)#Redondea a 160
print("a)",1000*a)
b = normal.cdf(182.25)-normal.cdf(171.25)#Redondea a 182 y 171.5
print("b)",1000*b)
c = normal.cdf(175.25)-normal.cdf(174.75)#Redondea a 175
print("c)",1000*c)
d = normal.sf(187.75)#Redondea a 188
print("d)",1000*d)

#Ejercicio 6.19 ****************************************
print("\nEjercicio 6.19 -------------------")
normal = stats.norm(15.9,1.5)

a = normal.cdf(16.225)-normal.cdf(13.745)
print("a)",a)
b = normal.isf(0.05)
print("b)",b)

#Ejercicio 6.20 ****************************************
print("\nEjercicio 6.20 -------------------")
normal = stats.norm(8,0.9)

a = normal.sf(9.55)
print("a)",a)
b = normal.cdf(8.65)
print("b)",b)
c= normal.cdf(9.15)-normal.cdf(7.25)
print("c)",c)

#Ejercicio 6.21 ****************************************
print("\nEjercicio 6.21 -------------------")
normal = stats.norm(10000,100)

a = normal.sf(10175)
print("a)",a)
b = normal.cdf(10225)-normal.cdf(9775)
print("b)",1-b)

#Ejercicio 6.22 ****************************************
print("\nEjercicio 6.22 -------------------")
mu = 0
sigma=1

normal = stats.norm(mu,sigma)

z1= mu + (1.3 *sigma)
z2= mu - (1.3 *sigma)
a = normal.sf(z1) + normal.cdf(z2)
print("a)",a)

z1= mu + (.52 *sigma)
z2= mu - (.52 *sigma)
b = normal.cdf(z1)-normal.cdf(z2)
print("b)",b)

#Ejercicio 6.23 ****************************************
print("\nEjercicio 6.23 -------------------")
normal = stats.norm(115,12)

a = normal.sf(94.5)
print("a)",600-(600*a))

