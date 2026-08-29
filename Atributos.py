#Para crear atributos de instancia se debe hacer lo siguiente

class Pajaro:

    alas = True
    #Aqui se definio el metodo constructor que nos dara los atributos
    def __init__(self, color, especie): #self seria el mismo y de ahi su atributo en este caso color
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("negro", "Tucan")
palabra = 'hola'
print( mi_pajaro.color)
print(mi_pajaro.especie)

print(f'mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')
print(mi_pajaro.alas)