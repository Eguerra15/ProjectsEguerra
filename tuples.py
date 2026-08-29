mi_tuple = (1,2,(10, 20) ,4)
print(type(mi_tuple))

#los tuples se pueden encontrar en diferente indice por lo tanto al poner un numero negativo hace que se cuente de
#derecha a izquierda

print(mi_tuple[-2])
#si quiero consultar el objeto que se encuentra en la posicion 2, debo de poner la pocision y el indice que busco

print(mi_tuple[2][0]) #aqui al poner indice dos estoy hablando de un tupple por lo tanto el 0 se refuere al indice del tupple

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1,2,3,1)

print(t.count(1))
print(t.index(3))

