"""
En este proyecto vamos a hacer un codigo que
describa la cantidad de sueldo que merece un
empleado dependiendo de su comision que es el
13% respecto a las ventas
"""
nombre = input("¿Cual es tu nombre completo?")
venta = input("¿Caunta es la cantidad que vendiste al mes?")

Comision = round(float(venta)*.13)
print(f"{nombre} La cantidad de comision que debes recivir es {Comision}"
      f"\n El valor total de tu sueldo sera {float(venta) + Comision}")
