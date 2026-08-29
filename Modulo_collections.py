from collections import Counter, defaultdict, namedtuple, deque

#Seccion de Counter
numero = [8,1,3,6,3,6,2,6,3,8,9]
print(Counter(numero))
#Con este metodo contamos los numeros que se encuentran en la lista y lo vuelve un diccionario

frase = 'al pan pan y al vino vino'
print(Counter(frase.split())) #Este metodo separa los elementos por los espacios en una lista

serie = Counter([1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5])
print(serie.most_common(2)) #Me esta mostrando los dos numeros con mas apariciones
print(list(serie)) #Ordeno los elementos en una lista sin repetir

 #Seccion de defaultdict
mi_dic = defaultdict(lambda: "nada")
mi_dic['uno'] = 'verde'
print(mi_dic['nada'])

#Seccion de namedtuple

Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.altura)
print(ariel[2])

#Seccion de deque
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
# Agregar "Atenas" al principio de la deque
lista_ciudades.appendleft("Atenas")
print(list(lista_ciudades)) #Podemos apreciar que se agrego Atenas en la izquierda