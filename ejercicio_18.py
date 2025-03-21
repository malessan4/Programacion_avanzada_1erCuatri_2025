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


# SUMA
def sumaFracciones(a, b):
    if a[1] == b[1]:
        sumaNumerador = a[0] + b[0]
        resultadoSumaD = sumaNumerador, b[1]
        return resultadoSumaD
    
    else:
        sumaNumerador = ( a[0] * b[1] ) + (b[0] * a[1])
        sumaDenominador = a[1] * b[1]
        resultadoSuma = sumaNumerador,  sumaDenominador
        return resultadoSuma
    
    
# RESTA
def restaFracciones (a,b):
    if a[1] == b[1]:
        restaNumerador = a[0] - b[0]
        resultadoRestaD = restaNumerador, a[1]
        return resultadoRestaD

    else:
        restaNumerador = ( a[0] * b[1] ) - (b[0] * a[1])
        restaDenominador = a[1] * b[1]
        resultadoResta = restaNumerador,  restaDenominador
        return resultadoResta
    
    
# MULTIPLICACION
def multiplicacionFraccion (a, b):
    multiNumerador = a[0] * b[0]
    multiDenominador = a[1] * b[1]
    resultadoMulti = multiNumerador , multiDenominador
    return resultadoMulti


# DIVISION
def divisionFraccion(a,b):
    if a[1] == b[1]:
        divisionNumerador = a[0] * a[1]
        divisionDenominador = a[1] * b[0]
        resultadoDenominadorD = divisionNumerador, divisionDenominador
        return resultadoDenominadorD

    else:
        divisionNumerador = a[0] * b[1]   
        divisionDenominador = a[1] * b[0]
        resultadoDivision = divisionNumerador,  divisionDenominador
        return resultadoDivision    

print("Bienvenidos/as a cuentas con Fracciones")
fragA = cargarFraccion()
fragB = cargarFraccion()

denominardorFraccion1 = denominadorFraccion(fragA)

numeradorFraccion1 = numeradorFraccion(fragB)

sumando = sumaFracciones(fragA, fragB)

restando = restaFracciones(fragA, fragB)

multiplicando = multiplicacionFraccion(fragA, fragB)

dividiendo = divisionFraccion(fragA, fragB)
print()

print(f'El denominador de la primera fraccion es: {denominardorFraccion1}')
print(f'El numerador de la segunda fracción es: {numeradorFraccion1}')

print()

print(f'La sumas de dichas funciones es: {sumando}')
print (f'La resta de dichas funciones es: {restando}')
print (f'La multiplicación de dichas funciones es: {multiplicando}')
print(f'La division de dichas funciones es {dividiendo}')