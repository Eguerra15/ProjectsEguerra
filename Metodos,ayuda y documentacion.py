"""En este apartado voy a investigar metodos nuevos"""

dic = {'clave' : 100, 'clave2': 500}

a = dic.popitem() #Este metodo elimina un elemento al alzar en los diccionarios
print(dic)

x = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

a = x.lstrip(",:_#").removesuffix(",,,,,,::#").replace("%","").replace("_ _"," ")
print(a)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja") #Inserta un elemento en una lista dependiendo la posicion que yo busque

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) #Devuelve True si no hay ningún elemento en el conjunto presente en el conjunto :xy

print(z)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

x = marcas_tv.isdisjoint(marcas_smartphones)
print(x)

x= 'hola mundo'
print(x.count('h'))
