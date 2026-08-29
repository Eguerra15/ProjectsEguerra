"""
EJERCICIO 1
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""

def devolver_distintos(a,b,c):
    total = 0
    lista = [a,b,c]
    for i in lista:
        total += i

    if total > 15:
        return max(lista)

    elif total < 10:
        return min(lista)
    elif total in range(10,15):
        lista.sort()
        return lista [1]
print(devolver_distintos(5,4,5))

"""
Ejercicio 2
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
"""

def aniquilador_ordenador(palabra):
    mi_set = set()

    for i in palabra:
        mi_set.add(i)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista
print(aniquilador_ordenador('hola'))

"""
Ejercicio 3

Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
"""
def repetidos_ceros(*args):
    mi_lista = []

    for i in args:
        mi_lista.append(i)
    if mi_lista.count(i)>1:
        return True
    return False
print(repetidos_ceros(1,4,3,2,0,0))

"""
Ejercicio 4
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números 
primos existentes en el rango que va desde cero hasta ese 
número incluido, y va a devolver la cantidad de números 
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
"""
#Pendiente de resolver

num = input('Dame un numero para sacar sus primos: \n')
x = int(num)
numeros_primos = []
def contar_primos(x):
    lista = list(range(0,x+1))
    print(f'Lista Original:\n{lista}')
    del lista[0:2]
    print(f'Lista con 0 y 1 sin considerar:\n{lista}')
    for i in lista:
        if i%2!=0:
            numeros_primos.append(i)
        else:
            continue
    return numeros_primos

numeros_primos = contar_primos(x)
print(f'los numeros primos son: \n{numeros_primos}')
