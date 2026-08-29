print("""****************************
    Primer Resultado
      """)
def suma():

    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2 "))
    print(n1 + n2)
    print('Gracias por sumar' + n1)

try:
    # Codigo que queremos probar
    suma()

except TypeError: #Le puedo añadir el codigo a ejecutar siempre y cuando haya un error de ese tipo
    # Codigo a ejecutar si hay un error
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    #Codigo a ejecutar si no hay un error(codigo adicional al try)
    print("Hiciste todo bien")
finally:
    #Codigo que se va a ejecutar de todos modos
    print("Eso fue todo")

print("""****************************
    Segundo Resultado
      """)
def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()