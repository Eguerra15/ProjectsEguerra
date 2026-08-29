class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, 'amarillo')
piolin.nacer()
print(piolin.color)
print(Pajaro.__bases__) #Este metodo me indica que base hereda la clase
print(Animal.__subclasses__())#Este metodo me dice a que funcion transmite su herencia

