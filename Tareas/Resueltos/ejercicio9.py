#Ejercicio 09
def Mcd():
    try:
        num_may = int(input("Digite el número mayor: "))
        num_men = int(input("Digite el número menor: "))
        resto = 0
        if num_men > num_may:
            num_men, num_may = num_may, num_men
        while num_may % num_men != 0:
            num_men, num_may = num_may % num_men, num_men
        print(f"El MCD es: {num_men}") 
    except Exception as e:
        print("El valor ingresado es erroneo") 

