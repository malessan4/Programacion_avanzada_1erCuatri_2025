# Calcular el área y el perímetro de un cuadrado, de un rectángulo y de una circunferencia.
# Realizar las invocaciones a las distintas funciones definidas anteriormente.

# Cuadrado
# Area = L elevando al cuadrado
# Perimetro = L*4

# Rectangulo
# Area = base * altura
# Perimetro = 2base + 2altura

# Circurferencia
# Area = 𝛑*Radio al cuadrado
# Perimetro = 2𝛑*radio

import math


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def areaCuadrado(self):
        resultado = self.lado ** 2 
        print(f'El area del cuadrado es: {resultado} ')
        
    def perimetroCuadrado(self):
        resultado = self.lado * 4
        print(f'El perimetro del cuadrado es: {resultado} ')
        
cuadrado1 = Cuadrado (2)
cuadrado1.areaCuadrado()
cuadrado1.perimetroCuadrado()

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def areaRectangulo(self):
        resultado = self.base * self.altura
        print(f'El area del rectangulo es: {resultado} ')
        
    def perimetroRectangulo(self):
        resultado = self.base * 2 + self.altura * 2
        print(f'El perimetro del rectangulo es: {resultado} ')

rectangulo1 = Rectangulo (4,8)
rectangulo1.areaRectangulo()
rectangulo1.perimetroRectangulo()



class Circurferencia:
    def __init__(self, radio):
        self.radio = radio
    
    def areaCircurferencia(self):
        resultado = math.pi * self.radio**2
        print(f'El area de la circurferencia es: {resultado} ')
        
    def perimetroCircurferencia(self):
        resultado = math.pi*2 * self.radio
        print(f'El perimetro de la circurferencia es: {resultado} ')
    
    
circurferencia1 = Circurferencia (6)
circurferencia1.areaCircurferencia()
circurferencia1.perimetroCircurferencia()