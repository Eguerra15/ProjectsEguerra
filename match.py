#match signidica coincidencia

serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie =='N-02':
    print('Nokia')
elif serie =='N-03':
    print('motorola')
else:
    print('No existe ese producto')

"""Esta es una nueva forma de usar un control de flujo"""
match serie:
    case 'N-01':
     print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
     print('motorola')
    case _:
        print('No existe ese producto')

"""Aqui comienza otro ejecrcio"""
cliente = {'nombre':'Federico',
           'edad': 45,
            'ocupacion': 'instructor'}

pelicula = {'titulo':'Matrix',
            'ficha_tecnica': {'protagonista':'Keanu reeves',
                              'director':'Lana y Lili Wachowski'}}

elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {'nombre':nombre,
              'edad':edad,
              'ocupacion':ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)

        case {'titulo':titulo,
              'ficha_tecnica' : {'protagonista':protagonista,
                                 'director':director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)

        case _:
            print("No se que es esto")






