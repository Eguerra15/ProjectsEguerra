lista = ['a' , 'b', 'c']

indice = 0

for item in lista :
    print(indice, item) #Esta no es la mejor manera de acceder al indice en python

    indice +=1

for item in enumerate(lista):
    print(item)

mis_tuples = list(enumerate(lista))
print(mis_tuples)

''' aqui empieza un ejercicio'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):

    print(f'{nombre} se encuentra en el índice {indice}')

''' aqui empieza un ejercicio'''

lista_indices = list(enumerate("Python"))
print(lista_indices)

''' aqui empieza un ejercicio
Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación,
que empiecen con M:'''

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):

    if nombre[0] == 'M':
        print(indice)

    else:
        pass