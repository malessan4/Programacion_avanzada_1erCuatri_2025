import math

def areaCuadrado(lado):
    resultado = lado ** 2 
    print(f'El area del cuadrado es: {resultado} ')
    
def areaRectangulo(base, altura):
    resultado = base * altura
    print(f'El area del rectangulo es: {resultado} ')
    
def areaCircurferencia(radio):
    resultado = math.pi * radio**2
    print(f'El area de la circurferencia es: {resultado} ')
    
    
lado = int(input("Ingrese el lado del cuadrado "))

base = int(input("Ingrese la base del rectangulo "))
altura = int(input("Ingrese la altura del rectangulo "))

radio = int(input("Ingrese el radio del circulo "))

areaCuadrado(lado)
areaRectangulo(base, altura)
areaCircurferencia(radio)