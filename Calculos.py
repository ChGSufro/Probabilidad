import math

euler = math.e

datos1 = [
    1.00836411110671, 1.19249564133253, 0.0720715752907951, 0.841301284097895, 
    0.241000278391662, 0.0758542107440413, 0.34095061243617, 0.705441908482272, 
    0.963516199031365, 0.924430064035259, 0.369095412057743, 0.861445481120339, 
    0.672715728227001, 1.17445746127691, 0.215646684835383, 1.04890153127605, 
    0.407784504954656, 0.955460373490517, 0.688073129938906, 0.856013280453048, 
    0.0409280540149978, 0.687778615533889, 0.793566486304283, 0.899093247914338, 
    0.378640640796103, 1.13044906605984, 0.794099258074376, 1.52421787580016, 
    1.15139730727415, 0.341434012653336
]

print("""
    Ejercicio 1
""")

print("La suma de los datos es: " + str(sum(datos1)))
promedio1 = sum(datos1) / len(datos1)
print("El promedio es: " + str(promedio1))
estimador1 = promedio1 / 2
print("El estimador es: " + str(estimador1))

evaluacion_probabilidad1 = (1/pow(euler, 1/estimador1)) * (-1 - (1/estimador1)) 
evaluacion_probabilidad2 = (1/pow(euler, 1/(2*estimador1))) * (-1 - 1/(2 * estimador1))
probabilidad = evaluacion_probabilidad1 - evaluacion_probabilidad2

print("La probabilidad es: " + str(probabilidad))

print("""
    Ejercicio 2
""")

datos2 = [
    10.7407138596728, 10.3920210964855, 10.7187624641385, 13.734325292706, 
    12.6217419775159, 13.6571147163401, 11.3337387610172, 11.8496460172693, 
    10.5456686276157, 11.2051541011893, 9.53553335070154, 14.5641667738344, 
    8.57220086169678, 11.7799155020415, 12.8346096101397, 10.9140839944601, 
    12.2622492528252, 12.1970268352682, 9.20594960286882, 11.9333297033936, 
    7.07755597282644, 15.431488186066, 13.9939009606615, 12.5751092811258, 
    9.78882193239114
]

promedio2 = sum(datos2) / len(datos2)

def varianza():
    resulrado = 0
    for dato in datos2:
        resulrado += pow(dato - promedio2, 2)
    return resulrado / len(datos2)

def varianza_1():
    resulrado = 0
    for dato in datos2:
        resulrado += pow(dato - promedio2, 2)
    return resulrado / (len(datos2) - 1)

print("El estimador 1 es: " + str(promedio2))
print("El estimador 2 es: " + str(varianza()))

print(varianza_1())

sqrt = math.sqrt(varianza_1()/25)
t_tudent = 2.797
intervalo1 = promedio2 + (t_tudent * sqrt)
intervalo2 = promedio2 - (t_tudent * sqrt)

print("El intervalo de confianza es: " + str(intervalo2) + " - " + str(intervalo1))

mu = 13.1
z = (promedio2 - mu) / sqrt
print("El valor de z es: " + str(z))

intervalo3 = (24 * varianza_1()) / 39.364
intervalo4 = (24 * varianza_1()) / 12.401

print("El intervalo de confianza es: " + str(intervalo3) + " - " + str(intervalo4))

print("""
    Ejercicio 3
""")

datos3 = [
    15.9773504243157, 13.2334656421423, 8.07903934341825, 13.7499364502847, 
    12.785573257671, 11.5662597373287, 10.914526284841, 14.7708118974886, 
    11.551589732932, 16.3053004011265, 15.9880127254766, 14.6836564172445, 
    11.8742185572055, 9.44585831427549, 12.0685758660204, 14.5365226524662, 
    10.2154322311879, 12.2999800417654, 9.72215347347185, 13.1965106060038, 
    15.7381734639224, 11.4793300992219, 11.7040107554034
]

promedio3 = sum(datos3) / len(datos3)

print("El valor del estimador mu es: " + str(promedio3))

def varianza3():
    resulrado = 0
    for dato in datos3:
        resulrado += pow(dato - promedio3, 2)
    return resulrado / len(datos3)

def varianza3_1():
    resulrado = 0
    for dato in datos3:
        resulrado += pow(dato - promedio3, 2)
    return resulrado / (len(datos3) - 1)

print("El valor del estimador sigma es: " + str(varianza3()))

sqrt3 = math.sqrt(varianza3_1()/23)   
t_tudent3 = 2.074
intervalo5 = promedio3 + (t_tudent3 * sqrt3)
intervalo6 = promedio3 - (t_tudent3 * sqrt3)

print("El intervalo de confianza es: " + str(intervalo6) + " - " + str(intervalo5))


intervalo7 = (22 * varianza3_1()) / 36.781
intervalo8 = (22 * varianza3_1()) / 10.982

print("El intervalo de confianza es: " + str(intervalo7) + " - " + str(intervalo8))
