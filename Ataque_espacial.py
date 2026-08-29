import pygame
import random
import math
from pygame import mixer #Libreria de sonido
import io

"""FUNCION QUE TRANSFORMA LA FUENTE A OBJETO BYTES"""
def fuentes_bytes(fuente):
    #Abre el archivo TTF en modo lectura binaria
    with open(fuente,'rb') as f:
        #lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    #Crea un objeto BytesIO a partir de los bytes del archivo TTF
    return io.BytesIO(ttf_bytes)

"""INICIALIZAR PYGAME"""

pygame.init() #Con esto inicializo las herramientas de pygame
"""CREAR UNA PANTALLA"""
pantalla = pygame.display.set_mode((800, 600)) #Pantalla sea igual a establecer el modo en que se muestra en pygame 800x600 pixeles

#Todo lo que ocurra en una pantalla de pygame es un evento

"""TITULO E ICONO"""
pygame.display.set_caption("Invasión espacial") #Cambia el nombre del titulo de pantalla
icono = pygame.image.load("ovni.png") #Con este codigo cargo la imagen al codigo y la guardo en una variable
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

"""AGREGAR MUSICA"""
mixer.music.load('MusicaFondo.mp3') #Musica de fondo
mixer.music.set_volume(0.6)
mixer.music.play(-1) #Se puso -1 para que se repita cada vez que termine


"""JUGADOR VARIABLES"""
img_jugador = pygame.image.load("Nave.png")#Con este codigo cargo la imagen al codigo y la guardo en una variable
jugador_x = 368 #Posicion del personaje en x
jugador_y = 520#Posicion del personaje en y
jugador_x_cambio = 0
jugador_y_cambio = 0
def jugador(x , y):
    pantalla.blit(img_jugador,(x , y)) #Arrojar el jugador en la pantalla

"""ENEMIGO VARIABLES"""
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))  # Con este codigo cargo la imagen al codigo y la guardo en una variable
    enemigo_x.append(random.randint(0, 736))  # Posicion del personaje en x
    enemigo_y.append(random.randint(50, 200))  # Posicion del personaje en y
    enemigo_x_cambio.append(0.4)
    enemigo_y_cambio.append(50)  # Bajara 50 pixeles


def enemigo(x , y,ene):
    pantalla.blit(img_enemigo[ene],(x , y))

"""BALA VARIABLES"""
balas = []
img_bala = pygame.image.load("missile.png")#Con este codigo cargo la imagen al codigo y la guardo en una variable
bala_x = 0#Posicion del personaje en x
bala_y = 500#Posicion del personaje en y
bala_x_cambio = 0
bala_y_cambio = 0.7
bala_visible = False

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+ 16,y + 10))

"""PUNTAJE"""
puntaje = 0
fuente_como_bytes = fuentes_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font('FreeSansBold.ttf',30)
texto_x = 10
texto_y = 10

def mostras_puntaje(x,y):
    texto = fuente.render(f'Puntaje:{puntaje}',True,(255,255,255))#Renderizar, o sea imprimir en pantalla
    pantalla.blit(texto,(x,y))


"""TEXTO FINAL DE JUEGO"""
fuente_final = pygame.font.Font(fuente_como_bytes,40)
def texto_final():
    mi_fuente_final = fuente_final.render('VALES PINGA',True,(255,255,255))
    pantalla.blit(mi_fuente_final,(230, 270))

"""FUNCION DETECTAR COLICIONES"""
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_1 - y_2,2)) #Formula de la distancia entre dos puntos
    if distancia < 27:
        return True
    else:
        return False

#Este codigo lo dejamos a ultimo, pues mantiene el display abierto
"""LOOP DEL JUEGO"""
se_ejecuta = True

while se_ejecuta:
    #imagen de fondo
    """pantalla.fill((205, 144, 228)) """ # Fill quiere decir relleno, o sea colores en el display
    pantalla.blit(fondo,(0,0)) #Arroja una imagen deltro de la pantalla

    #Iterrar eventos
    for evento in pygame.event.get(): #Revisara cada uno de los eventos de la cola de elementos .get
        """Evento cerrar"""
        if evento.type == pygame.QUIT: #Si el evento es tipo quit, finalizara nuestro programa y cerrara la pantalla
            se_ejecuta = False

        """Evento precionar flechas"""
        if evento.type == pygame.KEYDOWN: #KEYDOW significa tecla precionada
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.4

            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.4

            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3') #Aqui cargamos un sonido
                sonido_bala.set_volume(0.7)
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -1
                }
                balas.append(nueva_bala)

                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        """Evento soltar flechas"""
        if evento.type == pygame.KEYUP: #KEYUP identifica si el usuario suelta una tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0 #Vuele el cambio en 0 para que deje de producir movimiento


    """Modificar ubicacion del jugador"""
    jugador_x += jugador_x_cambio

    """Mantener bordes al jugador"""
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    """Modificar ubicacion del enemigo"""
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
        #Fin del juego
        if enemigo_y[e] > 495:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()


        """Mantener bordes al enemigo"""
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.25
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.25
            enemigo_y[e] += enemigo_y_cambio[e]
        """Colision"""
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("disparo.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(30, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    """Movimiento bala"""
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)



    jugador(jugador_x,jugador_y)

    mostras_puntaje(texto_x,texto_y)

    """Actualizae"""
    pygame.display.update() #Con este metodo actualizo los datos