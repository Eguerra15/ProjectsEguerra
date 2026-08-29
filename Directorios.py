import os

#metodo que obtiene el directorio de trabajo actual
"""
ruta = os.getcwd()
"""
#Establece una ruta distinta de trabajo, un archivo que se encuentra en otro lugar
"""
ruta = os.chdir('C:\\Users\\emili\OneDrive\\Escritorio\\Capeta Alternativa')
"""

#Permite establecer una rota o crear una carpeta nueva
"""
ruta = os.makedirs('C:\\Users\\emili\OneDrive\\Escritorio\\Capeta Alternativa\\otra')
"""

#Este es un metodo OS con lo metodos basename
ruta = 'C:\\PhytonTotal\\Dia 6\\prueba.txt'

elemento = os.path.basename(ruta) #Pide el nombre de base de nuestra ruta
elemento1 = os.path.dirname(ruta) #nos dara la primera parte de nuestra ruta
elemento2 = os.path.split(ruta) #nos trae una topla que primero tiene el nombre d eruta y luego el de base

print(elemento)
print(elemento1)
print(elemento2)

#si quiero eliminar un directorio uso este metodo
"""os.rmdir('C:\\Users\\emili\\OneDrive\\Escritorio\\Capeta Alternativa\\otra')"""

otro_tecto = open('C:\\Users\\emili\\OneDrive\\Escritorio\\Capeta Alternativa\\otro_tecto.txt')
print(otro_tecto.read())

#con estos metodospodemos abrir un archivo sin importar el sistema operativo que maneje

from pathlib import Path

carpeta = Path('/Users/emili/OneDrive/Escritorio/Capeta Alternativa') / 'otro_tecto.txt'

mi_archivo = open(carpeta)
print(mi_archivo.read())