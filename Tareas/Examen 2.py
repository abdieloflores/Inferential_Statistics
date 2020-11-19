from scipy import stats

print("\n--------- EXAMEN SEGUNDO PARCIAL ---------")

#************ EJERCICIO 1 ************
print("\nEJERCICIO 1 ************")
normal = stats.norm(0,1)

#P(.68 < z < 1.43)
a = normal.cdf(1.43)-normal.cdf(0.68)
print(" a)",a)
#P(.58 < z < 1.74)
b = normal.cdf(1.74)-normal.cdf(0.58)
print(" b)",b)
#P(0.44 < z < 1.55)
c = normal.cdf(1.55)-normal.cdf(0.44)
print(" c)",c)
#P(z < 1.34)
d = normal.cdf(1.34)
print(" d)",d)
#P(z < 4.32)
e = normal.cdf(4.32)
print(" e)",e)

#************ EJERCICIO 2 ************
print("\nEJERCICIO 2 ************")
normal = stats.norm(10,2)

#P(x > 13.5)
a = normal.sf(13.5)
print(" a)",a)
#P(x < 8.2)
b = normal.cdf(8.2)
print(" b)",b)
#P(9.4 < x < 10.6)
c = normal.cdf(10.6)-normal.cdf(9.4)
print(" c)",c)

#NORMALIZADO
print("\n - NORMALIZADO\n")
normal = stats.norm(0,1)
#P(z > 1.75)
a = normal.sf(1.75)
print(" a)",a)
#P(z < -0.9000000000000004)
b = normal.cdf(-0.9000000000000004)
print(" b)",b)
#P(-0.2999999999999998 < z < 0.2999999999999998)
c = normal.cdf(0.2999999999999998)-normal.cdf(-0.2999999999999998)
print(" c)",c)

#************ EJERCICIO 3 ************
print("\nEJERCICIO 3 ************")
normal = stats.norm(1200,99)
#P(x > 1300)
a = normal.sf(1300)
print(" a)",a)
#P(x > 1500)
b = normal.sf(1500)
print(" b)",b)

#NORMALIZADO
print("\n - NORMALIZADO\n")
normal = stats.norm(0,1)
#P(z > 1.0101010101010102)
a = normal.sf(1.0101010101010102)
print(" a)",a)
#P(z > 3.0303030303030303)
b = normal.sf(3.0303030303030303)
print(" b)",b)

#************ EJERCICIO 4 ************
print("\nEJERCICIO 4 ************")

# P(X^2>\chi^2_\alpha)=0.1 cuando v=30
chi_2 = stats.chi2(30)
a = chi_2.isf(0.01)
print(" a)",a)
print("   * Comprobacion:",chi_2.sf(chi_2.isf(0.01)))

# P(X^2<\chi^2_\alpha)=0.9 cuando v=5
chi_2 = stats.chi2(5)
b = chi_2.ppf(0.9)
print(" b)",b)
print("   * Comprobacion:",chi_2.cdf(chi_2.ppf(0.9)))

# P(\chi^2_\alpha<X^2<23.209)=0.15 cuando v=0.15
chi_2 = stats.chi2(10)
c = chi_2.ppf(chi_2.cdf(23.209)-0.15)
print(" c)",c)
print("   * Comprobacion:",chi_2.cdf(23.209)-chi_2.cdf(chi_2.ppf(chi_2.cdf(23.209)-0.15)))


#************ EJERCICIO 5 ************
print("\nEJERCICIO 5 ************")

s=20
n=20
mu=74
sigma=8

x = ((n-1)*s)/sigma

print(" X^2 = ",x)

chi_2 = stats.chi2(n-1)
a = chi_2.isf(0.01)
print(" P(X^2>\chi^2_\alpha)=0.1 ", a)

print("\n No es un valor valido")

