monedas = 5

while monedas > 0: #mientras que las monedas sean mayor a 0
    print(f"Tengo {monedas} monedas")

    monedas -= 1

else: print("No tengo mas dinero")

"""Aqui esta otro ejemplo"""

RESPUESTA = 's'

while RESPUESTA == 's':
    RESPUESTA = input("quieres seguir? (S/N)" )

else:
    print("Gracias")

"""Aqui esta otro ejemplo"""
respuesta = 's'

#while respuesta == 's':
   # pass #Se encarga para guardar un espacio para el programador
#print("hola")      """Los pase a comentario para poder trabajar"""

"""Aqui esta otro ejemplo"""

nombre = input("Tu nombre:")

for letra in nombre:
    if letra == 'r':
        break #aqui interrumpe la iteracion pero no el loob
        print(letra)

"""Aqui esta otro ejemplo"""

nombre = input("Tu nombre:")

for letra in nombre:
    if letra == 'r':
        continue #aqui continuara con la iteracion
        print(letra)