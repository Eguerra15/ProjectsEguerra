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

mi_ruta = Path(Path.home(), "Recetas")
base = Path.home()
print(f"""Hola, bienvenido al recetario virtual

La ruta de acceso de tu base es: 
¨{base}
""")


# Contar recetas guardadas en el sistema
def contar_archivos(archivo):
    contador = 0
    for txt in Path(archivo).glob("**/*.txt"):
        contador += 1
    return f"Cantidad de recetas guardadas: {contador}"


print(contar_archivos(mi_ruta))
print("---------------------------------")

# Ejecuto la linea de accion del sistema
def inicio():
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("""¿Que acción gusta realizar?
            [1] - Leer receta
            [2] - Crear recete
            [3] - Crear categoria
            [4] - eliminar receta
            [5] - eliminar categoria
            [6] - finalizar programa""")
        eleccion_menu= input()
        system('cls')

    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("categorias:")
    ruta_categorias = Path(ruta)
    lista_categoria = []
    contador = 1

    for carpeta in ruta_categorias.iterdir(): #Este metodo muestra los subdirectorios del programa
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categoria.append(carpeta)
        contador += 1

    return lista_categoria

def elegir_categorias(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria:")
    system('cls')
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'): #Se aplica el metodo glob para encontrar todos los archivos que terminan en txt
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = "x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1,len(lista) + 1):
        eleccion_receta = input("\n Elige una receta:")
    system('cls')
    return lista[int(eleccion_receta) - 1]

def leer_recete(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva,contenido_receta)#Este metodo escribe un nuevo texto que esta compuesto por una ruta y una data que tiene que ser un string
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True

        else:
            print("Esta receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input() + ".txt"
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva) #Crea un nuevo directorip
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True

        else:
            print("Esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink() #Con este metodo elimino un archivo
    print(f"La receta {receta.name} ha sido eliminada ")

def eliminar_categoria(categoria):
    Path(categoria).rmdir() #Remove directori
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = "x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\n Precione V para volver al menu:")
    system('cls')
finalizar_programa = False
while not finalizar_programa:

    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas)< 1:
            print("no hay recetas en esta categoria.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_recete(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:

        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu == 6:
        finalizar_programa = True

inicio()






