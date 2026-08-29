class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muu")

class Oveja():
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")

Vaca1 = Vaca('Aurora')
Oveja1 = Oveja('Nube')

Vaca1.hablar()
Oveja1.hablar()

#Esto nos permite el polimorfismo, en una iteracion llamar a cada uno de estos objetos de formas
#distintas pero hacerles ejercutar el metodo que se llame igual aunque haga cosas distintas
animales = [Vaca1, Oveja1]

for animal in animales:
    animal.hablar()

print("""****************************
    Primer Resultado
      """)


#Otro ejemplo para entenderlo
def animal_habla(Oveja1):
    Oveja1.hablar()

animal_habla(Oveja1)
print("""****************************
    Segundo Resultado
      """)
#Otro ejemplo de polimorfismos
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for indices in [palabra, lista, tupla]:
    print(len(indices))
print("""****************************
    Tercer Resultado
      """)
#Otro ejemplo para entenderlo
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

legolas = Mago()
arturo = Arquero()
yaho = Samurai()
personajes = [arturo,legolas,yaho]

for ataques in personajes:
    ataques.atacar()
print("""****************************
    Cuarto Resultado
      """)
#Otro ejemplo para entenderlo
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

legolas = Mago()
arturo = Arquero()
yaho = Samurai()
def personaje_defender(personaje):
    personaje.defender()

personaje_defender(legolas)
print("""****************************
    Quinto Resultado
      """)