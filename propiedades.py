""""""
nombre = "Carina"
#nombre[o] = "k" Aqui estoy mal pues los strings no se pueden cambiar
print(nombre)
""""""""
n1 = "Kari"
n2 = "na"
print(n1 + n2)
""""""
n1 = "Kari"
print(n1*5) #los strings se pueden multiplicar
""""""
poema = """Mil pequeños peces blancos 
como si hirviera 
el color del agua """ #Esta es una forma de hacer saltos de linea sin \n

print(poema)

#Tambien puedo indetificar si un resultado se encuentra en el texto
print("agua" in poema)

#Tambien puedo preguntar si algun resultado no esta en el texto
print(("sol" not in poema))

#Tambien podemos identificar el largo de algun string con la funcion lend
print(len(poema))