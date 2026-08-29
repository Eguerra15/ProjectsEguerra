texto = "ABCDEFGHIJKLM"
fracmento = texto[2:10:2] #El ultimo : indica los saltos que da
print(fracmento)

texto = "ABCDEFGHIJKLM"
fracmento = texto[::-1]
print(fracmento)

frase = "Controlar la complejidad es la esencia de la programación"
fracmento= frase[:9]
print(fracmento)

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fracmento=frase[8::3]
print(fracmento)

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fracmento=frase[::-1] #con este metetodo pusimos el texto de un orden contrario, se invirtio
print(fracmento)


