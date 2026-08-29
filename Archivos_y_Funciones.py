"""Crea una función llamada abrir_leer() que abra (open) un archivo
indicado como parámetro, y devuelva su contenido (read)."""


def abrir_leer(archivo):
    archivo1 = open(archivo)
    return archivo1.read()

print(abrir_leer("prueba.txt"))

"""Crea una función llamada sobrescribir() que abra (open) un archivo indicado
como parámetro, y sobrescriba cualquier contenido anterior por el texto 
"contenido eliminado" """

def sobrescribir(archivo):
    documento = open(archivo,"w")
    documento.writelines("contenido eliminado")
    return documento.read()

"""Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro,
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
Finalmente, debe cerrar el archivo abierto."""

def registro_error(archivo):
    documento = open(archivo,"a")
    documento.write("se ha registrado un error de ejecución")
    documento.close()
