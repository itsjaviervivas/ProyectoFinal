 #-*-coding: UTF-8-*-
#Este programa será nuestro Traductor.
#Leer diccionario
import math
import sys

diccionario = open('diccionario.txt', encoding ='ISO-8859-1')
leer = diccionario.read()
listadiccionarios = leer.split("\n")

def distance(str1, str2):
    """ """
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



correctas = []
correccion= []
def revisar (diccionario, word):

    if word in diccionario:
        correctas.append(word)
        print("la palabra", word.upper(), "está correctamente escrita")
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
                print(diccionario[posicion[i]], end = ".")
                print()
        respuesta = input("La palabra que necesitas, ¿Se encuetra en la lista de posibles palabras? ")
        if "si" == respuesta:
                                 lista = int(input("En que posicion se encuentra: "))
                                 restar = lista-1
                                 buscar = diccionario[posicion[restar]]
                                 correccion.append(buscar)
        elif "no"== respuesta:
            print("En nuestro diccionario no se ecuentra la palabra que buscas")
        else:
            print("Ingresó una palabra invaldia, gracias por usar nuestro corrector")
            sys.exit()
    print()
    


               
while True:
    general = correctas + correccion
    print ("la corección es: " , end="")
    for i in ((general)):
        print(i, "" , end = "")

    print()
    print()
    
    print("Bienvenidos al corrector ortográfico.")
    """El programa le pregunta al usuario como prefiere utilizar el programa."""
    entrada = input("Seleccione una opción: \nsi: Archivo texto.txt\nno: Archivo Ingresado\nexit: Salir del programa\n")
    #convierte todo lo que el usuario ingrese a minúscula.
    entrada2 = entrada.lower()

    signos = "!\"#$%&’()*+,-./:;<=>?@[\\]^_‘{|}~"
    def remover(s):
         r = ""
         for letra in s:
            if letra not in signos:
                 r += letra
         return r


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
        remove = "",remover(entradaT)
        print (remove)
        e=remove.split(' ')
         
        
        for i in range(len(e)):
            revisar(listadiccionarios, e[i].lower())

    
                 
                 
    elif entrada2 == "exit":
        sys.exit()
    else:
        print("Ingrese una opción valida. Solo Si o No.")
        print("¡Hasta pronto!")


print("(C) 2018 Ángela & Javier")

