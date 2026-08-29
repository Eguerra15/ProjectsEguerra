#Metodo de instancia
class Pajara:
    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}') #Con este metodo cambio las llaves por el atributo de mi clase

    def volar(self,metros):
        print(f'El pajaro a volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    # Metodos de clase
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajara.alas)

    #Metodos estaticos
    @staticmethod
    def mirar():
        print('El pajaro mira')

Piolin = Pajara('amarillo','canario')
Piolin.pintar_negro()
Piolin.volar(50) #los metodos de instancia pueden invocar otros objetos
Pajara.poner_huevos(3) #Metodo clase no necesita una instacia para ejecutarse
Pajara.mirar()#Metodo estatico

#Ejemplo de metodo Estatico
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Perro = Mascota()
Perro.respirar()

#Ejemplo de metodo de clase
class Jugador():
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(Jugador.vivo)

Emi = Jugador()
Emi.revivir()

#Ejemplo ded metodo de intancia
class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(f'{self.cantidad_flechas}')
Meliodas = Personaje(5)
Meliodas.lanzar_flecha()