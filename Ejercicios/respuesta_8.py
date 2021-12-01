lista = []
print("Ingrese números, y para salir ingrese \"basta\"")
while True:
    valor = input("Ingrese un valor: ")
    if valor == "basta":
        break
    else: 
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("Dato invalido")
            exit()

resultado = 0
for x in lista:
    resultado += x

print(resultado)