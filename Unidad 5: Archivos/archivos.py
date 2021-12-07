from io import open
import os

texto = "Esto es una cadena\n Esto es otra cadena"

archivo = open("chanchito_2.txt","w")

archivo.write(texto)

archivo.close() 

archivo2 = open("/home/statick/Desarrollo/curso_python_nov2021-main/Unidad 5/chanchito_2.txt","w")

texto2 = "Esto es otro texto que voy a agregar al documento\n Este es el último cambio"

archivo2.write(texto2)

#archivo2.read()



archivo2.close()

#archivo3 = open("chanchito_3.txt", "x")

#os.remove("chanchito_3.txt")
os.rmdir("prueba_eliminar")
#os.mkdir()
