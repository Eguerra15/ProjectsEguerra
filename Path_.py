from pathlib import Path

#Este metodo lo vueleve una ruta alternativa

"""base = Path.home()"""
#De esta forma creo una ruta absoluta, siempre y cuando ponga la base primero
"""guia = Path(base,"Europa","España","Barcelona","Sagrada_Familia")"""
"""print(base)"""

#Se le añade un nombre a la ruta
"""guia2 = guia.with_name("La_pedrera.txt")"""

#Este metodo devuelve el antecesor mas inmediato de una ruta de archivos determinada
"""print(guia.parent.parent.parent)"""

"""print(guia)"""
"""print(guia2)"""


guia = Path(Path.home(),"Europa")

#significa glob como global
for txt in Path(guia).glob("**/*.txt"): #De esta manera muestro los txt que se encuentra
    print(txt)

print("----------------------------------------------") #Simple separacion
#El metodo Relative to es muy util cuando se desea recuperar una porcion de una ruta larga

guia = Path("Europa", "españa","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","España"))
print(en_europa)
print(en_espania)
