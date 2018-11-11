#Este programa será nuestro Traductor.
# -*- coding: UTF-8 -*-


print("Bienvenidos al corrector ortográfico.")
entrada = input("El texto que quieres corregir es un archivo txt?  ")
if entrada == "si": 
            archivo = input("¿Cómo se llama el archivo?")
            arc = archivo+ ".txt"
            try :
                my_file = open(arc, "r")
                mensaje = my_file.read()
                txt = mensaje.split(' ')
                print (txt)
                my_file.close()
            except TypeError:
                print ("No hay ningún archivo con ese nombre")
            if entrada == "no": 
                texto = input ("Ingrese el el texto que quieres corregir:  ")
            else: 
                print("ingresó una opción inválida" , "Se acabó el programa")
else:
    entrada2 = input(" Ingrese el texto : " )
    e2 = entrada2.split(' ')
    print (e2)
