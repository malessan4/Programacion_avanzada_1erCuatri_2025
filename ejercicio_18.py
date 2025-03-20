def cargarFraccion():
    numerador = int(input('Ingrese el numerador: '))
    denominador = int(input('Ingrese el denominador: '))
    fraccion = []
    fraccion.append(numerador)
    fraccion.append(denominador)
    return fraccion

def numeradorFraccion(fraccion):
    return fraccion[0]

def denominadorFraccion(fraccion):
    return fraccion[1]


