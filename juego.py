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
    #2
    print("Segunda oración: Deberías mirar hay a ver que ay: ")
	a = "Deberías mirar ahí a ver que hay."
	b = "Deberías mirar ay a ver que hay."
	c = "Deberias mirar ahi a ver que hay."

	print ("Opciones \n" ,"a)", a +"\n" , "b)" , b+"\n" , "c)" ,  c+"\n" )	  
	respuesta1 = input("¿Cuál es la correcta?: ")	
	if respuesta1 == "a": 
		print("La respuesta es correcta", " \n" , "La correción es Deberías mirar ahí a ver que hay.")	
	elif respuesta == " b" :
		print ("La respuesta es incorrecta" , "\n" , "Porque, la expresión 'ay' se usa para exclamar." + "\n" + "La correción es Deberías mirar ahí a ver que hay." )
	else: 
		print ("La respuesta es incorrecta", "\n", "Porque, la palabra 'ahí' lleva tilde en al 'i'."+"\n"+ "La correción es Deberías mirar ahí a ver que hay.")
    #3
    print("Tercera oración: Tu dejastes una marca en mi corazon: ")
	a = "Tu dejastes una marca en mi corazón"
	b = "Tú dejaste una marca en mi corazón"
	c = "Tu dejaste una marca en mi corazon"

	print ("Opciones \n" ,"a)", a +"\n" , "b)" , b+"\n" , "c)" ,  c+"\n" )	  
	respuesta1 = input("¿Cuál es la correcta?: ")	
	if respuesta1 == "a": 
		print("La respuesta es incorrecta", " \n" , "Porque, 'Tú' lleva tilde cuando queremos indicar a la persona con la que hablamos" , "\n" , "Por otro lado, 'Dejaste' nunca lleva 's' al final.", "\n", "La correción es Tú dejaste una marca en mi corazon")	
	elif respuesta == " b" :
		print ("La respuesta es correcta" , "\n" , "La correción es Tú dejaste una marca en mi corazón" )
	else: 
		print("La respuesta es incorrecta", " \n" , "Porque, 'Tú' lleva tilde cuando queremos indicar a la persona con la que hablamos" , "\n" , "Por otro lado, 'Dejaste' nunca lleva 's' al final y 'corazón' lleva tilde.", "\n", "La correción es Tú dejaste una marca en mi corazon")	
    #4
    print("Cuarta oración: El transplante se llevara acabo en un par de días: ")
	a = "El trasplante se llevará a cabo en un par de días."
	b = "El transplante se llevará a cabo en un par de días."
	c = "El trasplante se llevará acabo en un par de días"

	print ("Opciones \n" ,"a)", a +"\n" , "b)" , b+"\n" , "c)" ,  c+"\n" )	  
	respuesta1 = input("¿Cuál es la correcta?: ")	
	if respuesta1 == "a": 
		print ("La respuesta es correcta . La correción es El trasplante se llevará a cabo en un par de días.")
	elif respuesta == " b" :
		print ("La respuesta es incorrecta" , "\n" , "Porque, la expresión 'transplante' no existe. Su uso correcto es: Trasplante." + "\n" + "La correción es El trasplante se llevará a cabo en un par de días." )
	else: 
		print ("La respuesta es incorrecta" , "\n" , "Porque, se utiliza la expresión 'acabo' en referencia al efecto o cumplimiento de algo. También como conjugación del verbo acabar." + "\n" + "La correción es El trasplante se llevará a cabo en un par de días." )
    #5
    print("Quinta oración: Haya encontraremos la paz: ")
	a = "Halla encontraremos la paz."
	b = "Aya encontraremos la paz."
	c = "Allá encontraremos la paz."

	print ("Opciones \n" ,"a)", a +"\n" , "b)" , b+"\n" , "c)" ,  c+"\n" )	  
	respuesta1 = input("¿Cuál es la correcta?: ")	
	if respuesta1 == "a": 
		print("La respuesta es incorrecta", " \n" , "Porque, 'Halla' es una conjugación del verbo hallar." , "\n" , "La correción es Allá encontraremos la paz.")	
	elif respuesta == " b" :
		print ("La respuesta es incorrecta" , "\n" , "Porque, es un sustantivo femenino que significa ‘mujer encargada en una casa del cuidado y educación de los niños o jóvenes, según la RAE.’'" + "\n" + "La correción es La correción es Allá encontraremos la paz." )
	else: 
		print ("La respuesta es correcta . La correción es Allá encontraremos la paz.")
