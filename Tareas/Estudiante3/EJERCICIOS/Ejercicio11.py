"""
Escribir un programa que lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, 
pero no si es divisible por 100, excepto que también sea divisible por 400
"""
entrada=int(input("Ingrese el año: "));

if entrada%400==0 or (entrada%4==0 and entrada%100!=0):
    print("El anio ingresado es bisiesto");
else:
    print("El anio ingresado no es bisiesto");
    