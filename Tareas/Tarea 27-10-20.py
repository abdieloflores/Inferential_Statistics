from scipy import stats

#Ejercicio 6.2 ****************************************
print("\nEjercicio 6.2 -------------------")
    
uni = stats.uniform(1,5-1)
a = uni.cdf(4)-uni.cdf(2.5)
print("a)",a)   

#Ejercicio 6.3 ****************************************
print("\nEjercicio 6.3 -------------------")
    
uni = stats.uniform(7,10-7)
a = uni.cdf(8.8)
print("a)",a)
b = uni.cdf(9.5)-uni.cdf(7.4)
print("b)",b)
c = uni.cdf(10)-uni.cdf(8.5)
print("c)",c)

#Ejercicio 6.4 ****************************************
print("\nEjercicio 6.4 -------------------")
    
uni = stats.uniform(0,10-0)
a = 1-uni.cdf(7)
print("a)",a)
b = uni.cdf(7)-uni.cdf(2)
print("b)",b)

#Ejercicio 6.5 ****************************************
print("\nEjercicio 6.5 -------------------")

normal = stats.norm(0,1)

a = normal.cdf(-1.39)
print("a)",a)
b = normal.sf(1.96)
print("b)",b)
c = normal.cdf(-0.65)-normal.cdf(-2.16)
print("c)",c)
d = normal.cdf(1.43)
print("d)",d)
e = normal.sf(-0.89)
print("e)",e)
f = normal.cdf(1.74)-normal.cdf(-0.48)
print("c)",c)

#Ejercicio 6.6 ****************************************
print("\nEjercicio 6.6 -------------------")
normal = stats.norm(0,1)

a = normal.isf(0.3622)
print("a)",a)
print("    Comprobación:",normal.sf(normal.isf(0.3622)))
b = normal.ppf(0.1131)
print("b)",b)
print("    Comprobación:",normal.cdf(normal.ppf(0.1131)))
c = normal.ppf(normal.cdf(0)+0.4838)
print("c)",c)
print("    Comprobación:",normal.cdf(normal.ppf(normal.cdf(0)+0.4838))-normal.cdf(0))
d = normal.isf(0.0500/2)
print("d)",d)
print("    Comprobación:",normal.cdf(normal.isf(0.0500/2))-normal.cdf(-1*normal.isf(0.0500/2)))

#Ejercicio 6.7 ****************************************
print("\nEjercicio 6.7 -------------------")
normal = stats.norm(0,1)

a = normal.isf(0.2946)
print("a)",a)
print("    Comprobación:",1-normal.cdf(normal.isf(0.2946)))
b = normal.ppf(0.0427)
print("b)",b)
print("    Comprobación:",normal.cdf(normal.ppf(0.0427)))
c = normal.ppf(normal.cdf(-0.93)+0.7235)
print("c)",c)
c = normal.cdf(normal.ppf(normal.cdf(-0.93)+0.7235))-normal.cdf(-0.93)
print("    Comprobación:",c)

#Ejercicio 6.8 ****************************************
print("\nEjercicio 6.8 -------------------")
normal = stats.norm(30,6)
a = normal.sf(17)
print("a)",a)
b = normal.cdf(22)
print("b)",b)
c = normal.cdf(41)-normal.cdf(32)
print("c)",c)
d = normal.ppf(0.8)
print("d)",d)
x1 = normal.ppf(0.25/2)
x2 = normal.isf(0.25/2)
print("e) x1:",x1," x2:",x2)

#Ejercicio 6.9 ****************************************
print("\nEjercicio 6.9 -------------------")
normal = stats.norm(18,2.5)

a = normal.cdf(15)
print("a)",a)
b = normal.ppf(0.2236)
print("b)",b)
print("    Comprobación:",normal.cdf(normal.ppf(0.2236)))
c = normal.isf(0.1814)
print("c)",c)
print("    Comprobación:",normal.sf(normal.isf(0.1814)))
d = normal.cdf(21)-normal.cdf(17)
print("d)",d)

#Ejercicio 6.10 ****************************************
print("\nEjercicio 6.10 -------------------")
normal = stats.norm(0,1)

z1 = ((0-(3*1))-0)/1
z2 = ((0+(3*1))-0)/1

a= normal.cdf(z2)-normal.cdf(z1)
print("a)",a)

#Ejercicio 6.11 ****************************************
print("\nEjercicio 6.11 -------------------")
normal = stats.norm(200,15)

a = normal.sf(224)
print("a)",a)
b = normal.cdf(209)-normal.cdf(191)
print("b)",b)
c = normal.sf(230)
print("c)",1000*c)
d = normal.ppf(.25)
print("d)",d)

#Ejercicio 6.12 ****************************************
print("\nEjercicio 6.12 -------------------")
normal = stats.norm(30,2)
a = normal.sf(31.7)
print("a)",a)
b = normal.cdf(33.5)-normal.cdf(29.3)
print("b)",b)
c = normal.cdf(25.5)
print("c)",c)

#Ejercicio 6.13 ****************************************
print("\nEjercicio 6.13 -------------------")
normal = stats.norm(40,6.3)

a = normal.sf(32)
print("a)",a)
b = normal.cdf(28)
print("b)",b)
c = normal.cdf(49)-normal.cdf(37)
print("c)",c)

#Ejercicio 6.14 ****************************************
print("\nEjercicio 6.14 -------------------")
normal = stats.norm(10,0.03)

a = normal.sf(10.075)
print("a)",a)
b = normal.cdf(10.03)- normal.cdf(9.97)
print("b)",b)
c = normal.ppf(.15)
print("c)",c)

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
