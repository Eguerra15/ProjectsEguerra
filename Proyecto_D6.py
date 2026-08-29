"""Crear un recetario el cual cumpla con lo siguiente

-La bienvenida de usuario
-La ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas
-nos informara cuantas recetas hay en total dentro de la carpeta
-Pedira que eliga una de las sig opciones
    [1]-Leer receta
    [2]-Crear receta
    [3]-Crear categoria
    [4]-eliminar receta
    [5]-eliminar categoria
    [6]-finalizar programa
"""

from os import system
from pathlib import Path
import os

carpeta = Path(Path.home(),"Recetas")
base = Path.home()
print(f"""Hola, bienvenido al recetario virtual
        
La ruta de acceso de tu base es: 
¨{base}
""")

#Contar recetas guardadas en el sistema
def contar_archivos(archivo):
    contador = 0
    for txt in Path(archivo).glob("**/*.txt"):
        contador += 1
    return f"Cantidad de recetas guardadas: {contador}"

print(contar_archivos(carpeta))
print("---------------------------------")

Ejecutar = int(input("""¿Deseas ejecutar el sistema?
[1]-Si
[2]-No
"""))


#Ejecuto la linea de accion del sistema
def Ejecutar_sistema(numero):
    if numero == 1:
        system("cls")
        x= int(input( """ ¿Que acción gusta realizar?
    
    [1]-Leer receta
    [2]-Crear recete
    [3]-Crear categoria
    [4]-eliminar receta
    [5]-eliminar categoria
    [6]-finalizar programa"""))
        system("cls")
        return x
    else:
        print("¡Ok, adiós!")
#Le doy una accion real al sistema
def lector(eleccion):
    if eleccion == 1:
        opcion = int(input("""¿Cual seccion quieres leer?
        [1]Carnes
        [2]Ensaladas
        [3]Pastas
        [4]Postres
        """))
        system("cls")
        if opcion ==1:

            carnes = Path(Path.home(),"Recetas","Carnes")
            print("Las recetas disponibles son:")
            for indice,txt in enumerate(Path(carnes).glob("*.txt")):
                print(f"[{indice}]{txt.stem}")
            receta = int(input("Eliga el numero de la receta que busca"))


    else:
        return "prueba"


numero = Ejecutar
eleccion = Ejecutar_sistema(numero)
print(lector(eleccion))
