"""Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar).
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado
del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera
(debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá",
y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia."""


from random import *

moneda = ["Cara", "Cruz"]
salvar = [randint(1, 10) for numero in range(6)]
print(salvar)
"#Lanzar la moneda aleatoriamente"
def lanzar_moneda(lista):
    cara = choice(lista)
    print(cara)
    return cara

#¿salvamos la lista o no?

def probar_suerte(resultado,lista):
    if resultado == 'Cara':
        lista= []
        print(f"la lista se autodestruira:\n {lista}" )
        return lista
    else:
        print(f"La lista fue salvada\n{lista}")
        return lista


resultado= lanzar_moneda(moneda)
probar_suerte(resultado, salvar)