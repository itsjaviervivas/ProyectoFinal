#juego para niños
#-*-coding: UTF-8-*-
entrada = int(input("¿Que edad tienes?: "))
puntaje = 0
if entrada< 10:
	print("Te vamos a dar diez oraciones, las cuales tienen errores ortográficos.") 
	print("Tendrás que completar con las oraciones con las posibles respuestas, al final te diremos tu puntaje y correción.")
	print ("¡Empezó el juego!")
	print("Primera oración: ¿Porque no estas estudiando?: ")
	a = "¿Por qué no estas estudiando?"
	b = "¿Porqué no estás estudiando?"
	c = "¿Por qué no estás estudiando?"

	print ("Opciones \n" ,"a)", a +"\n" , "b)" , b+"\n" , "c)" ,  c+"\n" )	  
	respuesta1 = input("¿Cuál es la correcta?: ")	
	if respuesta1 == "a": 
		print("La respuesta es incorrecta", " \n" , "Porque, 'estas' lleva tilde, ya que el verbo es el conjugado de 'estar'" , "\n" , "la correción es ¿Por qué no estás estudiando?")	
	elif respuesta == " b" :
		print ("La respuesta es incorrecta" , "\n" , "Porque, el porque de pregunta va separado y con tilde en la 'é'" + "\n" + "la correción es ¿Por qué no estás estudiando?" )
	else: 
		print ("La respuesta es correcta , la correción es ¿Por qué no estás estudiando?")
