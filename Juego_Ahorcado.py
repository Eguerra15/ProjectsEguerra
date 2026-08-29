"""
Crearemos el juego del ahorcado.

se le mostrara al jugador una serie de guines que representara la cantidad de indices de la palabra,
el jugador dira una letra, cada vez que se adivina una letra, se pone en la parte de la palabra,
si el jugador se equivoca perdera una vida
"""

from random import choice

palabras = 'valor comida jugar python web programacion perros mascota dinero lapiz telefono amor discos software libre propio cancion collar sol luna juguete españa escuela universidad'.split()
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

#Funcion que eligira la palabra de la lista
def elegir_palabra(lista_palabra):
    palabra_elegida = choice(lista_palabra)
    letras_unicas = len(set(palabra_elegida)) #contara cuantas letras unicas tiene nuestra palabra
    return palabra_elegida, letras_unicas

#Funcion que le pida al usuario una letra
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra:").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No se eligio una letra correcta")
    return letra_elegida

#mostraran pantalla el guion de cada letra
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)

        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))

#chequear si la letra que puso el usuario se encuentra o no
def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1

    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("ya has encontrado esa letra con intenta con otra diferente")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)
    return True
def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades, has encontrado la palabra !!")
    return True

palabra,letras_unicas = elegir_palabra(palabras)

while not juego_terminado: #Mientras que no sea verdad que juego se ha terminado
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos,terminado,aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado
