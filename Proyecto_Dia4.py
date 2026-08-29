"""juan esta pensando un numero del 1-10 tiene solo 8 intentos para adividar

a) si el numero que dijo el usuario es menor a uno o superior a 10, dira que ese numero no esta permitido
b) si el numero que dijo el usuario es menor al que penso el programa le dira que esta incorrecto
c)si el numero es mayor le dira al usuario que esta equivocado
d)si el usuario acierta el numero, le dira el programa cuantos intentos le tomo y que ha ganado
e) cada vez que el usuario pierda volvera a intentarlo hasta que gane
"""

from random import *

N_Computadora = randint(1,10)
intentos = 0
valor = 0


while intentos < 8:

    valor = int(input("¿Que numero estoy pensando?"))
    intentos += 1

    if N_Computadora == valor:
        print("Correcto!, adivinaste el numero que pensaba")
        print(f"Te costo un total de {intentos} intentos")
        break

    elif valor <= 0:
        print("Es incorrecto ese numero, prueba uno mas grande")
        intentos -= 1
    elif valor >= 11:
        print("Esta incorrecto ese numero,prueba uno mas chico")
        intentos-=1
    else:
        print("No estaba pensando en ese número")


else:
    print("Llegaste a tu limite de intentos")



