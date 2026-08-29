import time, timeit

def prueba_for(numero):

    lista = []

    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1

    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
#Modulo time para marcar el tiempo que ocurre entre la ejecucion de una parte del codigo y otra
inicio = time.time()
prueba_for(1500000)
final = time.time()
print(final - inicio)

inicio = time.time()
prueba_while(1500000)
final = time.time()
print(final - inicio)

#Modulo timeit para medir cuando dura la ejecucion de un codigo repitiendola muchas veces
declaracion = """
prueba_for(10)
"""
mi_setup = """
def prueba_for(numero):

    lista = []

    for num in range(1, numero + 1):
        lista.append(num)
    return lista
"""
duracion = timeit.timeit(declaracion,mi_setup,number = 100000)

print(duracion)

declaracion2 = """
prueba_while(10)
"""
mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1

    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion2 =timeit.timeit(declaracion2,mi_setup2,number = 100000)
print(duracion2)