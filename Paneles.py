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

#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)#frame significa CUADRO
panel_superior.pack(side=TOP) #Side es lado y TOP arriba

#etiqueda titulo
etiqueta_titulo = Label(panel_superior, text='sistema de facturacion', fg='azure4',
                        font=('Dosis',58), bg='burlywood',width=27) #label significa etiqueta, FG es color de frente
etiqueta_titulo.grid(row=0, column=0) #Grid significa cuadricula
#width significa ancho de la etiqueta

#panel izquierdo
panel_izquierdo = Frame(aplicacion,bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo,text='Comida',font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text='Bebidas',font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo,text='Postres',font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_calculadora.pack() #sie en defento no se pone nada en pack, se ira a la parte de arriba

#panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_recibo.pack() #sie en defento no se pone nada en pack, se ira a la parte de arriba

#panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT,bg='burlywood')
panel_botones.pack() #sie en defento no se pone nada en pack, se ira a la parte de arriba


#evitar que la pantalla se cierre
aplicacion.mainloop() #Hace que nuestra ventana se codifique sin cerrarse
