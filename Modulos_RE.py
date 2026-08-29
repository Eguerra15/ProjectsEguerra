import re

texto = "Si necesitas ayuda llama al (668)-598-9977 las 24 horas al servicio de ayuda online"

palabra = 'ayuda' in texto
patron = 'ayuda'

busqueda = re.search(patron,texto)


print(busqueda.span())#con este metodo busca la ubicacion de la palabra encontrada
print(busqueda.start())
print(busqueda.end())


print('\n EJEMPLO DE OTRA SECCION 1\n')
busqueda = re.findall(patron,texto)
print(busqueda)#Crea un alista con las apariciones de la palabra
print(len(busqueda))


for hallazgo in re.finditer(patron,texto): #Encontrar en una iteracion(finiter)
    print(hallazgo.span())
print(palabra)

"""
-----------------------------------------------------------------------
"""
print('\n EJEMPLO DE OTRA SECCION 2\n')
texto = "Llama al 564-525-6588 ya mismo"

patron = r'\d\d\d-\d{3}-\d\d\d\d'#la r al inicio se pone para mostrar que es un formato especial

resultado = re.search(patron,texto)
print(resultado)
print(resultado.group())#Con este metodo encontrara el valor que es igual al patron

texto1 = "Llama al 564-525-6588 ya mismo"
patron1 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado1 = re.search(patron,texto)
print(resultado1.group())
print('\n EJEMPLO DE OTRA SECCION 3\n')

"""
-----------------------------------------------------------------------
"""

clave = input("Clave: ")

patron = r'\D{1}\w{7}'
chequear = re.search(patron,clave)

print(chequear)

"""
-----------------------------------------------------------------------
"""

texto = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes',texto)
buscar1 = re.search(r'....demos',texto)#Los puntos son letras comodin que incluye cualquier cosa que incluya un espacio en el caracter
#La barra indica que no tiene que ser un digito
buscar2 = re.search(r'^\D$',texto)#El signo de moneda checara si no hay un digito al final del string
buscar3 = re.findall(r'[^\s]+',texto)#Todos los caracteres que no sean espacios vacios
print(buscar)
print(buscar1)
print(buscar2)
print(buscar3)

"""
-----------------------------------------------------------------------
"""

def verificar_email(email):
    # Expresión regular para validar un correo electrónico
    regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

    if re.match(regex, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
"""
-----------------------------------------------------------------------
"""

def verificar_saludo(frase):
    # Convertimos la frase a minúsculas para hacer la comparación
    frase_min = frase.lower()

    if frase_min.startswith("hola"):
        print("Ok")
    else:
        print("No has saludado")