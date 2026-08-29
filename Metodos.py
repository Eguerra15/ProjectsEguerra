class Pajara:
    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}') #Con este metodo cambio las llaves por el atributo de mi clase

    def volar(self,metros):
        print(f'El pajaro a volado {metros} metros')

piolin = Pajara('amarillo','canario')
piolin.volar(50)
piolin.piar()

#Otro ejemplo de metodos
class Perro:
    def __init__(self, raza):
        self.raza = raza

    def ladrar(self):
        print("Guau!")


Dog = Perro('Chihuahua')
Dog.ladrar()

#Otro ejemplo de metodos

class Alarma:

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


Reloj = Alarma()
Reloj.postergar(10)