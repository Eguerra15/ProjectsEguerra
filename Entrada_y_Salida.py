mi_archivo = open('prueba.txt')#Este metodo espera para abrir una serie de datos

#Este metodo lee el archivo que se usa
"""print(mi_archivo.read())"""
#Este metodo lee el archivo pero solo la primera linea
una_linea= mi_archivo.readline()
print(una_linea) #el sistema guarda el punto donde leyo la linea 1

una_linea= mi_archivo.readline()#el sistema guarda el punto donde leyo la linea 2
print(una_linea.rstrip())#Si no quiero que phyton me ejecute ese salto de linea uso rstrip()

una_linea= mi_archivo.readline()#el sistema guarda el punto donde leyo la linea 3
print(una_linea)

mi_archivo.close() #Hace que resguardes el espacio de memoria
"""
Tambien se pueden aplicar todos los metodos de strings
"""
mi_archivo = open('prueba.txt')

for linea in mi_archivo:
    print(f"Aqui dice: {linea}")
mi_archivo.close()
"""
Otro metodo que podemos trabajar 
"""
mi_archivo = open('prueba.txt')

#Con este metodo vuelvo el contenido de las lineas en lista
todas = mi_archivo.readlines()
print(todas)
mi_archivo.close()





mi_archivo.close() #Hace que resguardes el espacio de memoria