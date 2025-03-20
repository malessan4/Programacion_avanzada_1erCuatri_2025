def convertir_a_dolar(pesos):
    dolar = pesos / 1260
    print(f'La cantidad ${pesos} son USD ${dolar}')
    
def convertir_a_euro(pesos):
    euro = pesos / 1130
    print(f'La cantidad ${pesos} son Euros ${euro}')
    
def convertir_a_real (pesos):
    real = pesos / 190
    print(f'La cantidad ${pesos} son Reales ${real}')
    
pesos_a_cambiar = float(input('Ingrese la cantidad de pesos que va a cambiar: $'))

convertir_a_dolar(pesos_a_cambiar)
convertir_a_euro(pesos_a_cambiar)
convertir_a_real(pesos_a_cambiar)