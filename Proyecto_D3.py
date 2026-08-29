'''
crear un programa que pida al usuario imprimir un texto, luego pedira 3 tipos de letras
desde ese momento el programa dira:

¿cuantas veces aparecera cada letra en el texto?,
¿cuantas palabras hay a lo largo del texto?
¿Cual es la primera letra del texto y la ultima?
el sistema nos mostrara como se veria el texto si invertimos las palabras
el sistema nos dira si la palabra phyton se encuentra en la lista
'''

texto = input("escribe un texto: ").lower()#Aqui estoy pasando las letras que se presentan en el texto en minusculas
letras = [input("Por favor ingresa la primera letra: ").lower(), input("Por favor ingresa la segunda letra: ").lower(), input("Por favor ingresa la tercera letra: ").lower()]
print(letras)

contar_1 = texto.count(letras[0])
contar_2 = texto.count(letras[1])
contar_3 = texto.count(letras[2])
print(f"la cantidad de la primera letra es: {contar_1}")
print(f"la cantidad de la segunda letra es: {contar_2}")
print(f"la cantidad de la tercera letra es: {contar_3}")

Palabras = texto.split()#Aqui estoy dividiendo el texto por medio de sus espacios y los paso a una lista
print(f"La cantidad de palabras que hay: {len(Palabras)}")


letra_1 = texto[0]
letra_2 = texto[-1]
print(f"La primera letra del texto es: {letra_1} \n "
      f"la segunda letra del texto es: {letra_2}")

fracmento =  texto[::-1] #Este metodo hace que el texto tome un acomodo inverso
print(f"El texto al reves se se ve asi: \n{fracmento}")

Encontrar = print("phyton" in texto)
print(f"La palabra phyton se encuentra en la lista?: \n {Encontrar}")
