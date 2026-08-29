lista = ['a', 'b', 'c']

for letra in lista: #Por cada indice(letra) imprimir en lista "letra" : + letra
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista2 = ['pablo','laura','fede','luis','julia']

for nombre in lista2 :
    if nombre.startswith('l'): #Aqui determina este metodo si comienza con un determinado caracter, este caso l
        print(nombre)

    else:
        print('nombre que no comienza con L')

"""aqui es otro ejemplo"""
numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor)

"""aqui es otro ejemplo"""
palabra = 'phyton'

for letra in palabra:
    print(letra)

"""aqui es otro ejemplo"""

for a,b in [1, 2],[3,4],[5,6]: #se puede poner dos variables en el loop
    print(a) #aqui identifica el primer valor de la lista
    print(b) #aqui identifica el segundo valor de la lista

"""aqui es otro ejemplo"""
dic = {'clave': 'a ', 'clave2' : 'b' , 'clave3': 'c'}
for item in dic.items(): #con este metodo se imprime el item completo
    print(item)

for item in dic.values(): #con este metodo se imprime el valor completo
    print(item)

"""aqui es otro ejemplo"""

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero%2 ==0:
        suma_pares = suma_pares+numero
        print(f"suma par:\n{suma_pares}")


    else:
        suma_impares = suma_impares + numero
        print(f"suma impar:\n{suma_impares}")



