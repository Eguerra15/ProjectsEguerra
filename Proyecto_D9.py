import os
import re
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

#Esta sera la ruta de mi directorio
ruta = 'C:\\PhytonTotal\\Dia_9\\Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'

#Para ejecutar el dia que estas
hoy = datetime.date.today()

nros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo,patron):
    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return '' #Porque nuestra lista se llenaria con objetios none
def crar_listas():
    for carpeta, subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a),patron)
            if resultado != '':
                nros_encontrados.append((resultado.group())) #Queremos que nos de el grupo que encontro en ese resultado
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tN.SERIE')
    print('--------\t\t\t--------')

    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1

    print('\n')
    print(f'Numeros encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)}')
    print('-' * 50)



crar_listas()
mostrar_todo()