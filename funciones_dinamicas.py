'''Aqui esta un ejercicio'''

def chequear_3_cifras (lista):
 for n in lista:

    if n in range(100,1000):
        return True
    else:
        pass

 return False #Puse return afuera del ciclo para que cuando cheque que ninguna condicion se cumple, se vaya a return


resultado = chequear_3_cifras([55,99,6000])
print(resultado)

'''Aqui esta un ejercicio'''
def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:

        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return  lista_3_cifras
resultado = chequear_3_cifras([555,999,6000])
print(resultado)

"""Crea una función (todos_positivos) que reciba una lista de números como parámetro,
 y devuelva True si todos los valores de una lista son positivos, y False si al menos
  uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla."""

def todos_positivos (lista):
    for n in lista:
        if n <=0:
            return False

        else:
            pass

    return True
lista_numeros = todos_positivos([100,200,34])
print(lista_numeros)
"""Crea una función (suma_menores) que sume los números de una lista 
(almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000,
 y devuelva el resultado de dicha suma."""

lista_numero = [113,-3,102]

def suma_menores(lista_numero):
    suma = 0
    for n in lista_numero:
        if n >0 and n <1000:
            suma +=n

        else:
            pass
    return suma
print(suma_menores(lista_numero))

lista_numeros = [1, 50, 500, 5000, 750, 600]

'''Aqui es otra forma de resolver el ejercicio'''

def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma

"""Aqui inicia otro ejercicio"""

"""Crea una función (cantidad_pares) que cuente la cantidad de números pares
 que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta."""
lista_numero = [7,4,7,3,7,7,8]
cantidad = 0
def cantidad_pares(lista_numero):

    for numero in lista_numero:
        if numero%2==0:
            global cantidad
            cantidad +=1

        else:
            pass
    return cantidad
print(cantidad_pares(lista_numero))
"""Otra forma de hacer el ejercicio"""

lista_numeros = [7,4,7,3,7,7,8]

def cantidad_pares(lista_numeros):
    cantidad = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad
print(cantidad_pares(lista_numeros))