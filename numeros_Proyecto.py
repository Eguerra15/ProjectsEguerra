"""
generadores
decorador

"""

#Esta funcion contara los numeros que salgan de cosmeticos
def contador_C():
    num_c = 0
    while True:
        num_c += 1
        yield num_c
#Esta funcion contara los numeros que salgan de farmacia
def contador_F():
    num_f = 0
    while True:
        num_f += 1
        yield num_f

#Esta funcion contara los numeros que salgan de perfumeria
def contador_P():
    num_p = 0
    while True:
        num_p += 1
        yield num_p


numeracion_C = contador_C()
numeracion_F = contador_F()
numeracion_P = contador_P()

#Esta funcion dara el saludo del inicio
def inicio(funcion):

    def saludo(palabra):
        print("Toma tu turno:")
        funcion(palabra)
        print("Espera un momento")
    return saludo

#Imprime el catalogo de cosmeticos
@inicio
def catalogo_C(contar):
    print(f"\tC-{contar}")


#Imprime el catalogo de farmacia
@inicio
def catalogo_F(contar):
    print(f"\tF-{contar}")

#Imprime el catalogo de perfumeria
@inicio
def catalogo_P(contar):
    print(f"\tP-{contar}")

"""catalogo_C(next(numeracion_C))
catalogo_F(next(numeracion_F))
catalogo_P(next(numeracion_P))"""