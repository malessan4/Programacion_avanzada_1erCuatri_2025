class Dolar:
    def __init__(self, pesos):
        self.pesos = pesos
    
    def convertir_a_dolar():
        dolar = pesos / 1260
        print(f'La cantidad ${pesos} son USD ${dolar}')

class Euro:    
    def convertir_a_euro(pesos):
        euro = pesos / 1130
        print(f'La cantidad ${pesos} son Euros ${euro}')

class Real:    
    def convertir_a_real (pesos):
        real = pesos / 190
        print(f'La cantidad ${pesos} son Reales ${real}')
    
pesos_a_cambiar = float(input('Ingrese la cantidad de pesos que va a cambiar: $'))

cambio_a_dolar = Dolar
cambio_a_dolar.convertir_a_dolar(pesos_a_cambiar)

cambio_a_euro = Euro
cambio_a_euro.convertir_a_euro(pesos_a_cambiar)


cambio_a_real = Real
cambio_a_euro.convertir_a_real(pesos_a_cambiar)