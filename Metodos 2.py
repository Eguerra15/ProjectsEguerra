texto = "Este es el texto de federico"

resultado = texto.find("g") #Busca un determinado caracter dentro de mi string

#Cuando find no encuentra lo que buscas pone como resultado -1

print(resultado)

texto = "Este es el texto de federico"

resultado = texto.replace("e", "x") #reemplaza una variable por otra en el texto
print(resultado)

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."
resultado = texto.replace("difícil","facil").replace("mala","buena")

print(resultado)