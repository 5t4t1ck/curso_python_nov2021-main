"""
EJERCICIO 14.- Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el
producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de 
exclamación. Por ejemplo 5! = 1x2x3x4x5=120
"""

num = int(input("Ingresa un número:"))

fact = 1

for i in range(2, num+1):
    fact *= i
print("El resultado es : %d" % fact)
