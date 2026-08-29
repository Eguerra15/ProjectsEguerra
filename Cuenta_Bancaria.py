from os import system
class Persona:

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    pass
class Cliente(Persona):

    def __init__(self,nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):

        return f"{self.nombre} {self.apellido} \n#De cuenta = {self.numero_cuenta}  \nBalance: {self.balance} "
    def Depositar(self,monto):
        self.balance += monto
        print(f'se depositaron ${monto} a tu cuenta\nNuevo monto:{self.balance}')

    def Retirar(self,monto):
        if self.balance >= monto:
            self.balance -= monto
            print(f'se retiraron ${monto} a tu cuenta\nNuevo monto:{self.balance}')
        else:
            print('El monto a retirar excede tu cuenta')

def volver_inicio():
    eleccion_regresar = "x"
    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\n Precione V para volver al menu:")
    system('cls')
def Crear_cliente():
    nombre = input("Ingresa el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    balance = float(input("Ingrese el balance inicial: "))
    return Cliente(nombre,apellido,numero_cuenta,balance) #De esta manera le proporciono las variables a la clase

def Inicio():
    finalizar_programa = True
    while finalizar_programa:
        cliente = Crear_cliente() #Con este codigo acoplo las funciones para que trabajen entre si
        print(f'Bienvenido! \n{cliente}')
        print('Operaciones:')


        numero_operacion = "x"
        while not numero_operacion.isnumeric() or int(numero_operacion) not in range(1,3):
            print("""
            1.Depositar
            2.Retirar
            3.salir
            """)
            numero_operacion = input()

            if numero_operacion == "1":
                monto = float(input("Escriba el monto a depositar: "))
                cliente.Depositar(monto)
                volver_inicio()

            elif numero_operacion == "2":
                monto = float(input("Escriba el monto a retirar; "))
                cliente.Retirar(monto)
                volver_inicio()
            elif numero_operacion == "3":
                print("Hasta la proxima")
                finalizar_programa = False
                break

            else:
                print("Opcion no valida")


Inicio()
