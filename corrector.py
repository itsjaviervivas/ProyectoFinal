# -- coding: UTF-8 --
#Este programa será nuestro Traductor.

print("Bienvenidos al corrector ortográfico.")
"""El programa le pregunta al usuario como prefiere utilizar el programa."""
entrada = input("¿El texto que quieres corregir es un archivo .txt?:  ")
#convierte todo lo que el usuario ingrese a minúscula.
entrada2 = entrada.lower()

if entrada2 == "si" or entrada == "si ":
    #el usuario ingresa el nombre del archivo y el programa le agrega la extensión.
            archivo = input("¿Cómo se llama el archivo?: ")
            arc = archivo+ ".txt"
            #el programa buscará el archivo y lo leerá.
            try :
                my_file = open(arc, "r")
                mensaje = my_file.read()
                txt = mensaje.split(' ')
                print (txt)
                my_file.close()
            except TypeError:
                print ("No hay ningún archivo con ese nombre.")
#si el usuario ingresa un no el programa le pedirá que ingrese el texto.
elif entrada2 == "no" or entrada2 == "no ":
    entradaT = input("Ingrese el texto: " )
    #separa las palabras y las imprime a modo de lista.
    e2 = entradaT.split(' ')
    print (e2)
    
else:
    print("Ingrese una opción valida. Solo Si o No.")
    print("¡Hasta pronto!")


print("(C) 2018 Ángela & Javier")
