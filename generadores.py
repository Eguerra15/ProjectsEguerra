print("****Esta funcion no usa un generado****")
def mi_funcion():
    lista = []
    for x in range(1,6):
        lista.append(x*10)
    return lista
def mi_generador():
    for x in range(1,6):
        yield x * 10 #esta preparado para que cuando yo le pida el numero lo imprima en el momento

print(mi_funcion())

print("*****Esta funcion usa un generador*****")

print(mi_generador())

g = mi_generador()
print(next(g)) #Siguiente generador, ahora si podruce el siguiente del generador
print(next((g)))

print("***** Este es otro ejemplo de generadores*******")
def mi_generador2():
    x = 1
    yield x #Yield significa producir

    x += 1

    yield x

g =  mi_generador2()

print(next(g))
print("Texto que interrumpe")
print(next(g))

#Otro ejemplo
def mi_generador():
    num = 0
    while True:
        num += 1
        yield num


generador = mi_generador()
print(next(generador))


def restar_vidas():
    vidas = 4
    while True:
        vidas -= 1
        if vidas > 0:
            yield f'Te quedan {vidas} vidas'
        else:
            yield "Game Over"

perder_vida = restar_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
