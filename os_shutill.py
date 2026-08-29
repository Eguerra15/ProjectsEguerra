import os
import shutil
print(os.getcwd()) #Obtengo el directorio de trabjao actual

archivo = open('curso.txt','w')
archivo.write('texto de archivo')
archivo.close()

#Forma para mover un archivo a otro directorio
print(os.listdir()) #nos mostrara una lista de todos los archivos en el programa
"""shutil.move('curso.txt',"C:\\PhytonTotal\\Dia_8")""" #De esta manera reubico un archivo de un lugar a otro

#Forma para eliminar un archivo
"""os.rmdir()"""#Elimina una capeta vacia
"""shutil.rmtree""" #Elimina la carpeta de la ruta que pase de manera permanente(no se puede recuperar ni en papelera)

import send2trash

"""send2trash.send2trash('nombre_documento.txt')""" #Con este codigo traspaso un archivo txt a la papelera(el archivo debe estar en el paquete)

#Generador con rutas
print(os.walk('C:\\PhytonTotal\\Dia_9\\Carpeta_Superior'))
#walk almacena la ruta en donde se encutra, als subcarpetas y archivos que hay en esa carpeta, o sea va a crear 3 tuplas
ruta ='C:\\PhytonTotal\\Dia_9\\Carpeta_Superior'

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f'En la carpeta {carpeta}')
    print(f'las subcarpetas son:')
    for sub in subcarpeta:
        print((f'\t{sub}'))
    print('los archivos son:')
    for arch in archivo:
        print((f'\t{arch}'))
    print('\n')