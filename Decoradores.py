
print('*******Este es un ejemplo de decoradores*******')
def cambiar_letras(tipo):


    def mayuscula (texto):
        print(texto.upper())


    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula()

operacion = cambiar_letras('may')

operacion('palabra')

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayuscula (texto):
    print(texto.upper())

print("*******Aqui uso decoradres********")
@decorar_saludo
def minuscula(texto):
    print(texto.lower())

minuscula("Python")
print("******Aqui no uso decoradores*****")
mayuscula("python")

print("********Otra forma de activar el decorado********")
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayuscula (texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
print("******Aqui no uso decoradores*****")
mayuscula('emi')
print("*******Aqui uso decoradres********")
mayuscula_decorada('emi')