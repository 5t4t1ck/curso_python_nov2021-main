"""
Crea una aplicación que permita adivinar un número. 
En primer lugar la aplicación solicita un número 
entero por teclado. A continuación va pidiendo números 
y va respondiendo si el número a adivinar es mayor 
o menor que el introducido. El programa termina cuando 
se acierta el número.
"""
salida=None
numero=int(input("Ingrese numero: "))
while salida!="OK":
    numero2=int(input("Ingrese un numero entero: "))
    if numero2 > numero:
        print("El numero {numero2} ingresado es mayor ".format(numero2=numero2))
    elif numero2<numero:
         print("El numero {numero2} ingresado es menor ".format(numero2=numero2))
    else:
        print("El numero {numero2} ingresado es igual".format(numero2=numero2))
        break

