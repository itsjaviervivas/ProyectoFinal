 #-*-coding: UTF-8-*-
#Este programa será nuestro Traductor.
#Leer diccionario
import math
import sys

diccionario = open('diccionario.txt', encoding ='ISO-8859-1')
leer = diccionario.read()
listadiccionarios = leer.split("\n")

for i in range(len(listadiccionarios)):
    listadiccionarios[i] = listadiccionarios[i].split("/")[0]

def distance(str1, str2):
    d =dict()
    for i in range(len(str1)+1):
        d[i]=dict()
        d[i][0]=i
    for i in range(len(str2)+1):
        d[0][i] = i
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
    return d[len(str1)][len(str2)]
        
def revisar (diccionario, word):
    if word in diccionario:
        return True
    else:
        variable = math.inf
        posicion = []
        print("La palabra",word.upper(),"no se ha encontrado. Tenemos estas opciones: ")
        for i in range (len(diccionario)):
            actualDistance = distance(word, diccionario[i])
            if actualDistance == variable:
                posicion.append(i)
            elif actualDistance <= variable:
                variable = actualDistance
                posicion = [i]
        for i in range(len(posicion)):
            print(diccionario[posicion[i]], end=", ")
        print()
        print()
        return False
                
while True:
    print("Bienvenidos al corrector ortográfico.")
    """El programa le pregunta al usuario como prefiere utilizar el programa."""
    entrada = input("Seleccione una opción: \nsi: archivo texto.txt\nno: archivo ingresado\nexit: salir del prodrama\n")
    #convierte todo lo que el usuario ingrese a minúscula.
    entrada2 = entrada.lower()

    if entrada2 == "si" or entrada == "si ":
        #el usuario ingresa el nombre del archivo y el programa le agrega la extensión.
                
                arc = "texto.txt"
                #el programa buscará el archivo y lo leerá.
                try :
                    my_file = open(arc, "r")
                    mensaje = my_file.read()
                    txt = mensaje.split(' ')
                    my_file.close()
                    for i in range(len(txt)):
                        revisar(listadiccionarios, txt[i].lower())
            
                except TypeError:
                    print ("No hay ningún archivo con ese nombre.")
    #si el usuario ingresa un no el programa le pedirá que ingrese el texto.
    elif entrada2 == "no" or entrada2 == "no ":
        entradaT = input("Ingrese el texto: " )
        e2 = entradaT.split(' ')
        for i in range(len(e2)):
            revisar(listadiccionarios, e2[i].lower())
    elif entrada2 == "exit":
        sys.exit()
    else:
        print("Ingrese una opción valida. Solo Si o No.")
        print("¡Hasta pronto!")


print("(C) 2018 Ángela & Javier")

