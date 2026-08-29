"""TRABAJAREMOS CON **KWARGS """

def prueba(num1,num2,*args,**kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")

prueba(15,20,100,200,400,x='uno',y='dos',z='tres')

"""
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
"""

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

print(cantidad_atributos(x=1,y=2,z=3))

"""
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados
en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de
 este tipo.
"""

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

print(lista_atributos(x=1,y=2,g=5))

"""
Crea una función llamada describir_persona, que tome como parámetros su nombre y 
luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
"""

def describir_persona(nombre,**kwargs):
    print(f"Caracteristicas de {nombre}:")
    for caracter,valor in kwargs.items():
        print(f"{caracter}:{valor}")

print(describir_persona('Emi', pelo='negro',colorojos='cafe'))
