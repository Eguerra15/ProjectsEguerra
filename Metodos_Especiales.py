mi_lista = [1,1,1,1,1,1,1]
print(mi_lista)

class Objeto:
    pass

mi_objeto = Objeto()
print(mi_objeto) #De esta manera obtengo la representacion de la clase objeto

class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self): #Ayuda a definir la forma en que yo quiero que se manifieste un str de mi clase cada vez que el metodo lo requiera
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self): #Establece que sucedera cuando alguien pida el largo de los CD
        return self.canciones

    def __del__(self): #Agrega una impresion cuando el metodo del ocurre
        print('Se ha eliminado el CD')


mi_cd = CD('Pink Floyd', 'The wall', 24)
print(mi_cd) #Aqui se ejecuta el metodo __str__ hace que aparesca la informacion
print(len(mi_cd))#Aqui se ejecuta el metodo __len__

del mi_cd #Esta funcion eliminana alguna instancia
print("""****************************
    Primer Resultado
      """)
#Otros ejemplos
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'


mi_libro = Libro('principito', 'desconocido', 200)
print(mi_libro)

print("""****************************
    Segundo Resultado
      """)