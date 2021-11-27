"""
Crear un programa que me permita convertir un numero a letras
Tomemos en cuenta 3 valores
"""
numero = int(input("Por favor ingrese un valor de 1 a 3: "))

if numero == 1:
    print("Su valor {numero} es igual a: UNO".format(numero=numero))
elif numero == 2:
    print("Su valor {numero} es igual a: DOS".format(numero=numero))
elif numero == 3:
    print("Su valor {numero} es igual a: TRES".format(numero=numero))
else:
    print("Su valor {numero} está fuera de rango".format(numero=numero))
