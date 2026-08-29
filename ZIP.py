nombres = ['Ana','Hugo','Valeria']
edades = [65, 29, 42]
ciudades = ['mexico','lima', 'madrid']

combinados = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

''' aqui empieza un ejercicio'''

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado_1 = list(zip(capitales,paises))

for capital, pais in combinado_1:
    print(f"La capital de {pais} es {capital}")

''' aqui empieza un ejercicio'''

marcas = ['nike', 'adidas', 'redbull', 'cocacola']
productos = ['airforce1', 'messi' , 'checo' , 'fanta']

mi_zip = (zip(marcas, productos))
print(mi_zip)

''' aqui empieza un ejercicio'''


espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))
print(numeros)

