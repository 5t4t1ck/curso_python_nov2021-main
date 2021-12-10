# Ejercicio 07
def Login():
    usuario = "usuario1"
    clave = "asdasd"
    intento=1
    while intento <= 3:
        usr_aux = input("Digitar el usuario: ")
        pas_aux = input("Digitar la clave: ")
        if (usuario == usr_aux and clave == pas_aux):
            print("Acceso correcto!!")
            return
        else:
            print("Credenciales incorrectas, intente de nuevo!!")
            intento += 1
    if intento > 3:
        print("Ha superado los intentos permitidos, Adios")
    
