"""
Crea una consola de turnos para implementarla en una farmacia:

-Le preguntara al cliente cual de las areas desea dirigirse: cosmetica,farmacia,belleza
-le dara un numero de turno segun el area que se dirija, ejemplo C-54, dependiendo del area cambiara la letra
-nos preguntara siquiere que saquemos otro turno y repetiremos el proceso
-El mensaje de espera al cliente debe de tener texto adicional 'su turno es','espere un momento'

funciones
importar modulo
"""
from os import system
import numeros_Proyecto


def volver_inicio():
    eleccion_regresar = input("\nQuiere regresar?\n1)Si\n2)No")
    system('cls')
    return eleccion_regresar


def inicio1():
    copilar = True
    print("Bienvenido a Farmacia Eguerra")
    while copilar:

        area = 'x'
        while not area.isnumeric() or int(area) not in range(1, 4):
            area = input("Cual de las Area desea dirigirse? \n1)Cosmetica\n2)Farmacia\n3)Perfumeria\n ")

            if area == "1":
                numeros_Proyecto.catalogo_C(next(numeros_Proyecto.numeracion_C))

            elif area == "2":
                numeros_Proyecto.catalogo_F(next(numeros_Proyecto.numeracion_F))

            elif area == "3":
                numeros_Proyecto.catalogo_P(next(numeros_Proyecto.numeracion_P))

            else:
                print('*****Valor no valido*****')

        eleccion = volver_inicio()
        if eleccion == "2":
            copilar = False


inicio1()
