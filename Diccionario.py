diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario))

cliente = {'nombre': 'Juan', 'apellido': ' fuentes','peso': 88, 'talla' : 1.76}
consulta = (cliente['apellido'])
print(consulta)

dic = {'c1' : 55 , 'c2' :[10,20,30],'c3' : {'s1':100,'s2' : 200}}
print(dic['c2'][1]) #esta es una forma de hacer un diccionario  y ubicar
                     #un indice que contenga cierta informacion
                     #la primera pocision es la variable y la segunda el lugar

diccionario_ejercicio = {'c1' : ['a','b','c'], 'c2': ['d','e','f']}
print(diccionario_ejercicio['c2'][1].upper()) #de esta forma volvemos mayuscula una letra

dic = {1: 'a' , 2 : 'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)
print(dic.keys())
print(dic.values()) #valores actuales de un diccionario
print(dic.items())  #me dira todos los items que estan en el diccionario = o