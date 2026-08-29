if 10 > 9 :
    print('es correcto')


if 5 ==2:
    print('es correcto')

else:
    print('no es correcto')

mascota = 'perro'

if mascota == 'gato':
    print('tienes un gato')

elif mascota == 'perro' :
    print('tienes un perro')
else:
    print('no se que animal tienes')

''' aqui empieza un ejercicio'''
edad = 16
calificacion = 9

if edad < 18 :
    print('eres menor de edad')

    if calificacion >= 7:
        print('aprobado')
    else:
        print('no aprobado')

else:
    print('eres adulto')

''' aqui empieza un ejercicio'''
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:   #Elif es como agregar un afuncion mas o un if mas con la condicion de que sea antes del else
    print(f"{num1} y {num2} son iguales")

else:
    print(f"{num2} es mayor que {num1}")

''' aqui empieza un ejercicio'''

edad = 18
tiene_licencia = True

if edad >= 18:

    if tiene_licencia == True:
        print("Puedes conducir")

    else:
        print("No puedes conducir. Necesitas contar con una licencia")

else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

'''aqui empieza un ejercicio'''

habla_ingles = False
sabe_python =  True

if habla_ingles == True:

    if sabe_python == True:
        print("Cumples con los requisitos para postularte")


    else:
        print("Para postularte, necesitas saber programar en Python")

else:
    if sabe_python == True:
        print("Para postularte, necesitas tener conocimientos de inglés")

    else:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")





