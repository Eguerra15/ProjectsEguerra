import zipfile
import shutil

#METODO ZIPFILE
#De esta manera creo una carpeta tipo zip
"""
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('mi_texto_A.txt') #Puse el nombre del archivo que voy a incluir
mi_zip.write('mi_texto_B.txt')

mi_zip.close()"""

#Para descomprimir un archivo hago la siguiente linea de codigo

"""
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')
zip_abierto.extract() #Extrae solo un archivo el cual yo le indique
zip_abierto.extractall() #Extrae todos los archivos comprimidos que hay en la carpeta
"""

#METODO SHUTIL

#Primero creamos la ruta de la carpeta

carpeta_origen = 'C:\\PhytonTotal\\Dia_9\\Carpeta_Superior'

#Creamos el nombre de la capeta
archivo_destino = 'Todo_Comprimido'

#Con este metodo creare un archivo comprimido con la informacion que tiene mi archivo
shutil.make_archive(archivo_destino, 'zip',carpeta_origen)

#De esta manera descomprimo un archivo

shutil.unpack_archive('Todo_Comprimido.zip','Extraccion_Terminada', 'zip')