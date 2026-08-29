"""Aqui es un ejercicio diferente"""
def multiplicar (numero1,numero2):
    return numero1* numero2 #Return guarda un valor y te da un resultado

resultado = multiplicar(5,10) #puedo guardar los valores dados a una funcion en una variable

print(resultado)
"""Aqui es un ejercicio diferente"""
def multiplicar (numero1,numero2):
    total = numero1*numero2
    return total

print(resultado)

"""Aqui es un ejercicio diferente"""
def potencia(num1, exp):
    ecuacion = num1 ** exp
    return ecuacion

valor = potencia(2, 3)
print(valor)

"""Aqui es un ejercicio diferente"""
def usd_a_eur(num):
    conversion = num * .90
    return conversion


dolares = usd_a_eur(1)

"""Aqui es un ejercicio diferente"""
def invertir_palabra(arg):
    inversion_M = arg[::-1].upper()
    return inversion_M


x = invertir_palabra('Phyton')
print(x)