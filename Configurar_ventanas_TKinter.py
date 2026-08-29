from tkinter import *

#iniciar tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry('1020x630+0+0') #las ultimas sumas indican las coordenadas de nuestra ventana

#evitar maximizar
aplicacion.resizable(0,0)#en el eje x o y no se puede modificar la ventana

#titulo de la ventana
aplicacion.title('Mi restaurante - sistema de facturacion')

#color de fondo de la ventana
aplicacion.config(bg='burlywood') #Bg significa background

#evitar que la pantalla se cierre
aplicacion.mainloop() #Hace que nuestra ventana se codifique sin cerrarse

