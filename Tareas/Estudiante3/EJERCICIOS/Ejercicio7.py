"""
Realiza un programa que pida dos números ‘a’ y ‘b’ 
e indique si su suma es positiva, negativa o cero
"""

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))

resultado = a + b
if (resultado < 0 ):
    print ("El resultado de {a} + {b} es {total}, es un valor negativo".format(a=a,b=b,total=a+b))
else:
    print ("El resultado de {a} + {b} es {total}, es un valor positivo".format(a=a,b=b,total=a+b))