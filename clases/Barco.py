from clases import Case
from clases import Conventions
from itertools import product, repeat
from random import choice


instances = []
casillas_ocupadas = set()

def __init__(self, longitud):
        self.longitud = longitud
        self.orientacion = choice(Conventions.orientaciones)
        self.tocado = False
        self.hundido = False

        # performance / legibilidad:
        num_lineas = Conventions.tablero_num_lineas
        num_columnas = Conventions.tablero_num_columnas
        num2l = Conventions.generar_num_linea
        num2c = Conventions.generar_num_columna

def horizontal(self):
        while True:
            if self.orientacion == HORIZONTAL:
                rang = choice(range(num_lineas))
                primero = choice(range(num_columnas + 1 - longitud))
                letra = num2l(rang)
                cifras = [num2c(x) for x in range(primero, primero + longitud)]
                self.casillas = {Case.instances[l + c]
                              for l, c in product(repeat(letra, longitud), cifras)}
            else:
                rang = choice(range(num_columnas))
                primero = choice(range(num_lineas + 1 - longitud))
                cifra = num2c(rang)
                letras = [num2l(x) for x in range(primero, primero + longitud)]
                # Crear el barco
                self.casillas = {Case.instances[l + c]
                              for l, c in product(letras, repeat(cifra, longitud))}

def instancair(self):

            for existente in Barco.instances:
                if self.casillas.intersection(existente.casillas):
                    break  # break relativo al "for existente in barcos:"
            else:
                # Agregar el barco en el contenedor de barcos
                Barco.instances.append(self)
                # Informar la casilla que contiene un barco.
                for casilla in self.casillas:
                    casilla.barco = self
                # Agregar estas casillas a las casillas ocupadas :
                Barco.casillas_ocupadas |= self.casillas
                break  # break relativo al "while True:"

def generar_barcos(self):
        for longitud in Conventions.barcos_longitud:
            while True:
                barco = Barco(longitud)
                barco.horizontal()
                barco.instancair()
                
@classmethod
def generar_barcos(self.cls):
        for longitud in Conventions.barcos_longitud:
            self.longitud = longitud
