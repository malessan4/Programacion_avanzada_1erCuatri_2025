def calculo_litros(alto, ancho, profundidad):
    calculo_volumen = alto * ancho * profundidad
    volumen_a_litros = calculo_volumen * 1000
    print(f'La cantidad de litros que necesita es de {volumen_a_litros} litros')
    
alto_pileta = float(input('Ingrese el alto de la pileta: '))
ancho_pileta = float(input('Ingrese el ancho de la pileta: '))
profundidad_pileta = float(input('Ingrese la profundidad de la pileta '))

calculo_litros(alto_pileta, ancho_pileta, profundidad_pileta)