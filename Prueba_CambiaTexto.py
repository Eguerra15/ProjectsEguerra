import unittest
import Cambia_Texto

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self): #Se debe de poner la palabra test_ cada vez que quieres hacer una prueba
        palabra = "buen dia"
        resultado = Cambia_Texto.todo_mayusculas(palabra) #El metodo todo_Mayusculas se encuentra en "Cambiar texto"
        self.assertEqual(resultado,"Buen Dia") #Este metodo se encarga de checar 2 argumentos

#Esta seccion es obligatoria para que se pueda ejecutar el diferencidor de erro
if __name__ == '__main__':
    unittest.main()

