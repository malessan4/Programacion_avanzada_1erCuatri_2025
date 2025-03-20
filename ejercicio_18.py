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

"""
para la suma y resta primero tengo que ver si los denominadores son iguales o no
dependiendo eso se aplican diferentes procedimientos para la suma y resta
tengo que hacer que el resultado termine adentro de una lista
"""

def sumaFracciones(a, b):
    if a[1] == b[1]:
        sumaNumerador = a[0] + b[0]
        resultadoSumaD = sumaNumerador + b[1]
        return resultadoSumaD
    
    else:
        sumaNumerador = ( a[0] * b[1] ) + (b[0] * a[1])
        sumaDenominador = a[1] * b[1]
        resultadoSuma = sumaNumerador / sumaDenominador
        return resultadoSuma




print("Bienvenidos/as a cuentas con Fracciones")
fragA = cargarFraccion()
fragB = cargarFraccion()

denominardorFraccion1 = denominadorFraccion(fragA)

numeradorFraccion1 = numeradorFraccion(fragB)

sumando = sumaFracciones(fragA, fragB)

print(f'El denominador de la primera fraccion es: {denominardorFraccion1}')
print(f'El numerado de la segunda fracción es: {numeradorFraccion1}')
print(f'La sumas de dichas funciones es: {sumando}')