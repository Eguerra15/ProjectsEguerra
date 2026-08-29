"""Si queremos escribir un archivo existente se hace de estas formas"""
archivo = open('prueba.txt', 'w')
archivo.write("""hola
mundo
mi nombre
es 
emiliano""")
archivo.close()
#con este metodo escribo una lista concatenando las lineas
archivo = open('prueba.txt', 'w')
archivo.writelines(['hola','mundo','aqui','estoy'])
archivo.close()

#El ultimo metodo posiciona lo que planeo escribir al final
archivo = open('prueba.txt','a')
archivo.write('bienvenido')
archivo.close()