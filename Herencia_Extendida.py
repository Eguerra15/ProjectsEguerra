class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print('Este animal emite sonido')

class Pajaro(Animal):
    #Primera manera de añadir un atributo a una clase heredera
    def __init__(self,edad,color,altura_vuelo): #Se describen nuevamente los atributos
        """self.edad = edad
           self.color = color"""
        #El segundo metodo es con super, de esta manera no vuelvo a escribir sus atributos
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    #En esta seccion sobreescribe el metodo ya dado anteriormente
    def hablar(self):
        print('pio')
    def volar(self,metros):
        print(f'El pajaro vuela {metros} metros')
    pass

piolin = Pajaro(3,  'amarillo', 60)
mi_animal = Animal(5,'negro')
piolin.nacer()
piolin.volar(100)

print("****HERENCIA MULTIPLE******")

#La herencia multiple
class Padre():
    def hablar(self):
        print("hola puedo hablar")
    pass
class Madre():
    def reir(self):
        print('Ja ja ja')

    def hablar(self):
        print('que tal esto es de la madre')
class Hijo(Padre,Madre):#Si pongo madre primero, la herencia predominaria en la madre
    pass
class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir() #Aqui apreciamos que el nieto heredo de sus sucesores sus caracteristicas
mi_nieto.hablar() #Hereda la parte del  Padre porque primero hereda del dominante y luego de pasivo
print(Nieto.__mro__) #Con este metodo apreciamos el orden de resolucion de nuestra herencia
















