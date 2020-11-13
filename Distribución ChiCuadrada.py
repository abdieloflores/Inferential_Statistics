from scipy import stats
#help(stats.chi2)

#-----Ejemplo 1----------------------------------------------------
print("Ejemplo 1**************************************")

chi_2 = stats.chi2(15)

a = chi_2.isf(.025)
print("a:",a)
a = chi_2.sf(27.488392863442982)
print("a:",a)


chi_2 = stats.chi2(7) #Aqui esta los grados

b = chi_2.isf(.01) #Aqui utilizo isf para el valor de la variable aleatoria
print("b:",b)
b = chi_2.sf(18.475306906582365) #Aqui pongo el valor de la variable y me da el area?
print("b:",b)

#-----Ejemplo 2----------------------------------------------------
print("\nEjemplo 2**************************************")
chi_2 = stats.chi2(10)

# Lo hice asi profe, saque el punto x1 colocandoles de area .275 por que al 1 lequite el.
#.40 y lo divide entre 2 y ya despues el area restante la comprobe con cdf
# lo mismo realice con X2 pero con la funcion isf
# y al final comprobe los puntos X1 y X2 con cdf y me dio el .45
print("\n-------- X1 y X2 ---------")
a1 = chi_2.ppf(.275)
print("X1:",a1)
a2 = chi_2.cdf(7.004712389998741)
print("Area:",a2)
b1 = chi_2.isf(.275)
print("X2:",b1)
b2 = chi_2.sf(12.152192187104227)
print("Area:",b2)

c = chi_2.cdf(12.152192187104227)-chi_2.cdf(7.004712389998741)
print("Area Restante:",c)

#y aqui saque el area del primer punto que dio y le sume el .20 del area que se pedia
#y lo coloque en la funcion .ppf para que me diera X3
#Y ya solo comprobe el area restando las areas de los puntos con cdf

print("\n-------- X3 ---------")
chi_2 = stats.chi2(3)
a1 = chi_2.cdf(4.108)+.20
a2 = chi_2.ppf(a1)
print("X3:",a2)
c = chi_2.cdf(7.813132675463979)-chi_2.cdf(4.108)
print("Area Restante:",c)