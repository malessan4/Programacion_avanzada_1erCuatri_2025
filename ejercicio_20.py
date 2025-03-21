class Fraccion:
    def cargarFraccion():
        numerador = int(input('Ingrese el numerador: '))
        denominador = int(input('Ingrese el denominador: '))
        fraccion_lista = []
        fraccion_lista.append(numerador)
        fraccion_lista.append(denominador)
        return fraccion_lista

    def numeradorFraccion(fraccion_lista ):
        return fraccion_lista [0]

    def denominadorFraccion(fraccion_lista ):
        return fraccion_lista [1]


# SUMA
    def sumaFracciones(fragA, fragB):
        if fragA[1] == fragB[1]:
            sumaNumerador = fragA[0] + fragB[0]
            resultadoSumaD = sumaNumerador, fragB[1]
            return resultadoSumaD
    
        else:
            sumaNumerador = ( fragA[0] * fragB[1] ) + (fragB[0] * fragA[1])
            sumaDenominador = fragA[1] * fragB[1]
            resultadoSuma = sumaNumerador,  sumaDenominador
            return resultadoSuma
    
    
# RESTA
    def restaFracciones (fragA,fragB):
        if fragA[1] == fragB[1]:
            restaNumerador = fragA[0] - fragB[0]
            resultadoRestaD = restaNumerador, fragA[1]
            return resultadoRestaD

        else:
            restaNumerador = ( fragA[0] * fragB[1] ) - (fragB[0] * fragA[1])
            restaDenominador = fragA[1] * fragB[1]
            resultadoResta = restaNumerador,  restaDenominador
            return resultadoResta
        
        
# MULTIPLICACION
    def multiplicacionFraccion (fragA, fragB):
        multiNumerador = fragA[0] * fragB[0]
        multiDenominador = fragA[1] * fragB[1]
        resultadoMulti = multiNumerador , multiDenominador
        return resultadoMulti


# DIVISION
    def divisionFraccion(fragA,fragB):
        if fragA[1] == fragB[1]:
            divisionNumerador = fragA[0] * fragA[1]
            divisionDenominador = fragA[1] * fragB[0]
            resultadoDenominadorD = divisionNumerador, divisionDenominador
            return resultadoDenominadorD

        else:
            divisionNumerador = fragA[0] * fragB[1]   
            divisionDenominador = fragA[1] * fragB[0]
            resultadoDivision = divisionNumerador,  divisionDenominador
            return resultadoDivision    

print("Bienvenidos/as a cuentas con Fracciones")
fragA = Fraccion
fragA.cargarFraccion()

fragB = Fraccion
fragB.cargarFraccion()

denominardorFraccion1 = fragA.denominadorFraccion

numeradorFraccion1 = fragB.numeradorFraccion

fragA.sumaFracciones(fragA, fragB)

fragA.restaFracciones(fragA, fragB)

fragA.multiplicacionFraccion(fragA, fragB)

fragA.divisionFraccion(fragA, fragB)
print()

print(f'El denominador de la primera fraccion es: {denominardorFraccion1}')
print(f'El numerador de la segunda fracción es: {numeradorFraccion1}')

print()

print(f'La sumas de dichas funciones es: {fragA.sumaFracciones}')
print (f'La resta de dichas funciones es: {fragA.restaFracciones}')
print (f'La multiplicación de dichas funciones es: {fragA.multiplicacionFraccion}')
print(f'La division de dichas funciones es {fragA.divisionFraccion}')
