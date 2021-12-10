"""
Programa que lea un carácter por teclado y compruebe si es una letra mayúscula
"""

letra=input("Ingrese un caracter: ")

letraMay=letra.upper()

if(letra==letraMay):
    print("La letra{letra} ingresada es mayusculas".format(letra=letra))
else:
    print("La letra{letra} ingresada NO es mayusculas".format(letra=letra))
