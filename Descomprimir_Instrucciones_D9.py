import zipfile

#De esta manera descomprimire el archivo que cuenta con las instrucciones para el proyeto

archivo_descomprimido = zipfile.ZipFile('Proyecto+Dia+9.zip','r')
archivo_descomprimido.extractall()