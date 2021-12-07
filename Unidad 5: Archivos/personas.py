"""
1) En este ejercicio deberás crear un script llamado personas.py que lea 
los datos de un fichero de texto, que transforme cada fila en un diccionario 
y lo añada a una lista llamada personas. Luego rocorre las personas de la lista 
y para cada una muestra de forma amigable todos sus campos.

El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en 
texto plano (créalo previamente):

1;Carlos;Pérez;05/01/1989
2;Manuel;Heredia;26/12/1973
3;Rosa;Campos;12/06/1961
4;David;García;25/07/2006

Los campos del diccionario serán por orden: id, nombre, apellido y nacimiento.

Aviso importante: Si quieres leer un fichero que no se ha escrito directamente con Python, 
entonces es posible que encuentres errores de codificación al mostrar algunos caracteres. 
Asegúrate de indicar la codificación del fichero manualmente durante la apertura como 
argumento en el open, por ejemplo con UTF-8:

open(..., encoding="utf8")
"""
Carlos = {"id":1,"nobmre":"Carlos", "apellido":"Pérez", "fecha":"05/01/1989"}
Manuel = {"id":2,"nobmre":"Manuel", "apellido":"Heredia", "fecha":"26/12/1973"}
Rosa = {"id":3,"nobmre":"Rosa", "apellido":"Campos", "fecha":"12/06/1961"}
David = {"id":4,"nobmre":"David", "apellido":"García", "fecha":"25/07/2006"}

archivo = open("personas.txt","w")

archivo.write(str(Carlos))
archivo.write(str(Manuel))
archivo.write(str(Rosa))
archivo.write(str(David))

archivo.close()
