mi_lista = ['a', 'b', 'c']
resultado= len(mi_lista)
print(resultado)

mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

mi_lista3[0] = 'alfa' #aqui estoy sobrescribiendo el indice 0 que es 'a' a 'alfa'

mi_lista3.append('g') #append significa agregar, esto agrega un elemento

mi_lista3.pop() #pop interpreta que quieres eliminar el ultimo elemento
                # a no ser que tu pongas el indice que quieras eliminar

#tambien puedo guardar el elemento popeado en una variable

eliminado = mi_lista3.pop(2)
print(eliminado)
print(mi_lista3)

#tambien podemos ordenar las listas

listas = ['g','o','b','m','c']
listas.sort() #este metodo ordena los parametros pero no devuelve nada

print(listas)

#tambien podemos hacer las listas en reversa

listas.reverse()
print(listas)




