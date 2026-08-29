import datetime

mi_hora = datetime.time(17,35,50,1500)
print(mi_hora)

mi_dia = datetime.date(2025,10,17)
print(mi_dia)
print(mi_dia.year)
print(mi_dia.ctime())
print(mi_dia.today())#Muestra el dia de de hoy

#Para combinar fecha y hora

from datetime import datetime

mi_fecha = datetime(2025,5,15,22,10,15,2500)
print(mi_fecha)

mi_fecha = mi_fecha.replace(month=11) #De esta manera remplazo el parametro que yo busco
print(mi_fecha)

hoy = mi_fecha.today() #De esta manera almaceno la fecha actual
print(hoy)

minutos = datetime.now().minute
print(minutos) #Vuelve el tiempo que transcurre actualmente los minutos


#Calcular tiempos que transcurren de un momento a otro

from datetime import date

nacimiento = date(1995,3,5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento
print(vida)
print(vida.days)

#Si quiero saber un valor en horas
despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds) #De esta manera defino los segundos
