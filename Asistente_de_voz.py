import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#Opciones de voz/idioma
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

#escuchar nuestro microfono y devolver el audio como texto
def trasformar_audio_en_texto():

    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono

    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        #informar que comenzo la grabacion
        print('ya puedes hablar')

        #guardar lo que escuche como audio

        audio = r.listen(origen)

        try:
            #Buscar en google
            pedido = r.recognize_google(audio,language="es-MX")

            #pruebade que pudo ingresar
            print("Dijiste: "+ pedido)

            #devolver pedido
            return pedido

        #en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #Prueba de que no comprendio el audio
            print("ups, no entendi")

            #devolver error
            return "sigo esperando"

        #Error inesperado
        except:

            #prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            #devolver error
            return "sigo esperando"

#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    #Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice',id3)

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

def pedir_dia():

    #Crear variable con dia de hoy
    dia = datetime.date.today()
    print(dia)

    #Crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #Diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miercoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}
    #Decir dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#informar que hora es
def pedir_hora():

    #Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #Decir la hora
    hablar(hora)

#funcion de saludo
def saludo_inicial():

    #Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'

    elif 6 <= hora.hour < 13:
        momento = 'Buen dia'

    else:
        momento = 'Buenas tardes'

    #Decir el saludo
    hablar(f'{momento} ,soy Helena, tu asistente personal. Por favor, dime en que te puedo ayudar')

#funcion central del asistente
def pedir_cosas():

    #Activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:

        #Activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com') #Con esta funcion abre una aplicacion

        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')

        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es') #Este metodo establece un lenguaje en español en wikipedia
            resultado = wikipedia.summary(pedido,sentences =1) #summary quiere decir resumen, con sentences leera los parrafos 1 parrafo
            hablar('Wikipedia dice lo siguiente')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido) #esta funcion sirve para buscar en internet
            hablar('Esto es lo que he encontrado')
        elif 'reproducir' in pedido:
            hablar('¡Genia!, comenzare a reproducirlo')
            pywhatkit.playonyt(pedido) #Este metodo reproduce en youtube
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es')) #este medotodo nos da bromas
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de'[-1].strip()) #strip elimina los espacios en blanco
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'Encontre el precio de {accion}, es {precio_actual}')
                continue
            except:
                hablar('perdon pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Okay, me ire a descansar. Cualquier cosa que necesites puedes volver a decirme')
            break

pedir_cosas()




