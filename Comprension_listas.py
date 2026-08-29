palabra = 'phython'

lista = []

for letra in palabra:
    lista.append(letra)
print(lista)
'''aqui empieza un ejercicio'''
lista_2 = [letra_2 for letra_2 in palabra] #lista sea igual a una lista que cada letra sea igual a la variable palabra

print(lista_2)
'''aqui empieza un ejercicio'''
lista_3 = [n /2 for n in range(0,21,2) ]#puedo alterar el numero antes de incluirlos en mi lista
print(lista_3)
'''aqui empieza un ejercicio'''
lista_4 = [n  if n*2 > 10 else 'no' for n in range(0,21,2)] #tambien puedo añadir una condicion
print(lista_4)
'''aqui empieza un ejercicio'''
pies = [10, 20 , 30, 40 , 50]
metros = [p * 3.281 for p in pies]

print(metros)
'''aqui empieza un ejercicio'''
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [n for n in valores if n%2 == 0]
print(valores_pares)

'''aqui empieza un ejercicio'''
temperatura_fahrenheit = [32, 212, 275]

grados_celsius =[(grados_fahrenheit-32)*(5/9)  for grados_fahrenheit in temperatura_fahrenheit ]

print(grados_celsius)