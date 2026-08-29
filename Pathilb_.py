from pathlib import Path, PureWindowsPath

#purewindowsPath transforma cualquier ruta a una de windows

carpeta = Path('C:\\PhytonTotal\\Dia 6\\prueba.txt')

print(carpeta.read_text())
print(carpeta.name) #con este metodo nos muestra el nombre del archivo
print(carpeta.suffix) #nos muestra la terminacion del archivo
print(carpeta.stem) #nos muestra el nombre sin sufijo

if not carpeta.exists():
    print("Este archivo no existe")

else:
    print("Genial, existe")

carpeta = Path('C:/PhytonTotal/Dia 6/prueba.txt')
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)