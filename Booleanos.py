var1 = True
var2 = False
print(type(var1))

numero = 5 > 2 + 3
print(type(numero))
print(numero)

#podemos incluso hacer una funcion mucho mas explicita usando la funcion bool

numerp = bool (5<6) #si quieres generar un valor falso sin una variable necesaria solo deja bool() sin nada
print(type(numero))

lista = [1,2,3,4,5]
control = 5 not in lista
print(control)