"""
Pedir un número por teclado y mostrar la tabla de multiplicar
"""

numero = float(input("Ingrese un numero:"))
pregunta="SI"
contador=1.0
while pregunta=="SI":
    print ("{numero} x {producto} es: {resultado}".format(numero=numero,producto=contador,resultado=(numero*contador)))
    contador+=1.0
    if contador%10==0:
        pregunta=input("Desea continuar SI/NO: ")

