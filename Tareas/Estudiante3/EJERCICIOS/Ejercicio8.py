"""
Escribe un programa que lea un número e indique si es par o impar
"""

def par_impar(a):
    if (a%2==0):
           print("El numero {num} es par".format(num=numero1))
    else:
        print("El numero {num} es impar".format(num=numero1))

numero1= int(input("Ingrese numero: "))
par_impar(numero1)
