#Juego escoge el palito
import random
from random import shuffle #con esta libreria mezclaremos la lista

# Lista inicial
palitos = ['-','--','---','----']
# Mezclar palitos
def mezclar (lista):
    shuffle(lista)
    return lista

#pedirle intento

def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento =input('Elige un numero del 1 al 4: ')

    return int(intento)

intento1 = probar_suerte()
print(intento1)

#comprobar intento
def chequear_intento(lista,intento):
    if lista[intento-1]== '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f'te ha tocado {lista[intento-1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

"""
Aqui inicia otro ejercicio
Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
"""
from random import *
#Definir dados
caras = ['1','2','3','4','5','6']
dado1 = ''
dado2 = ''

#Arrojaremos los dados
def lanzar_dados (dado1,dado2):

    dado1 = int(choice(caras))
    dado2 = int(choice(caras))
    lista = [dado1,dado2]
    return lista

#sumar dados
suma_total = 0
def suma_dados(lista):
    suma_total =lista[0] + lista[1]
    return suma_total
#Evaluar jugada
def evaluar_jugada(suma_total):
    if suma_total<=6:
        print(f"La suma de tus dados es {suma_total}. Lamentable")

    elif suma_total in range(6,10):
        print(f"La suma de tus dados es {suma_total}. Tienes buenas chances")

    elif suma_total >=10:
        print(f"La suma de tus dados es {suma_total}. Parece una jugada ganadora")

    else:
        pass
    return suma_total
#juntar funcion

arrojar_dados = lanzar_dados(dado1, dado2)
Resultado = suma_dados(arrojar_dados)
evaluar_jugada(Resultado)
print(Resultado)


















