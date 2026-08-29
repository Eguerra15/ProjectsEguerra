from random import * #Al poner asterisco importo toda la libreria

#Es importante que las librerias no tengan el mismo nombre que la libreria pues ocurriria un error en estas

aleatorio = randint(1,10) #el primer indice indica el comienzo y el ultimo el limite
print(aleatorio)

aleatorio_1 = round(uniform(1,5),1) #nos da numeros aleatorios tipos float, puse un numero al final que indica el decimal
print(aleatorio_1)

aleatorio_2 = random() #este metodo siempre te dara un numero del 0 al 1 aleatoriamente
print(aleatorio_2)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio_3 = choice(colores) #Este metodo escoge un elemento presente en la lista el cual sea aleatorio
print(aleatorio_3)

numeros = list(range(5,50,5))
shuffle(numeros) #Es  te metodo hace una mezcla aleatoria en la lista, no se puede usar en strings
print(numeros)

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)