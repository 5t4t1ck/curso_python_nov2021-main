# Ejercicio 08
def Factorial():
    try:
        num = int(input("Digite el número a calcular: "))
        aux = 1
        for factor in range(1, num+1):
            aux = factor * aux
        print(f"El factorial de {num} es:", aux)
    except Exception as e:
        print("El valor ingresado es erroneo") 

