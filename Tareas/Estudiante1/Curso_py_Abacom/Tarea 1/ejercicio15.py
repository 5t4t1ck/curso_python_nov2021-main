"""
EJERCICIO 15.- Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número 
entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar 
es mayor o menor que el introducido. El programa termina cuando se acierta el número.
"""
secreto = int(input("Número secreto:"))
num = int(input("Número:"))

while num != secreto:

    if num > secreto:
        print("El número es menor")
    else:
        print("El número es mayor")

    num = int(input("Número:"))

print("Has acertado")
