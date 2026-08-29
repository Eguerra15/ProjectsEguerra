"""TRABAJAREMOS CON *ARGS"""

#Este codigo suma una cantidad infinita de numeros
def suma (*args):  #Los argumetos me permiten poner mas parametros de los deseados
    total = 0
    for arg in args:
        total += arg

    return total
print(suma(5,6,3,4,5,6))

#Esta funcion suma numeros elevados al cuadrado
def suma_cuadrados (*args):
    total = 0
    for numero in args:
        total += numero**2
    return int(total)
print(suma_cuadrados(2,3,5,-7))

#Esta funcion vuelve los numeros en absolutos y los suma
def suma_absolutos(*args):
    contador = 0
    for numero in args:
        contador += abs(numero)
    return contador

print(suma_absolutos(-3,-2))

#Esta funcion combina el uso de string y intergers en una funcion
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'

print(numeros_persona(input("tu nombre es: "),1,2,3))


