def a_pagar (personas, bebida, comida, alquiler):
    monto_gastado = bebida + comida + alquiler
    gasto_individual = monto_gastado / personas
    print(f'Se gasto {monto_gastado} y como son {personas} personas se debe pagar {gasto_individual} cada uno.')
    
personas = int(input('Ingrese la cantidad de personas que son: '))
bebida = float(input('Ingrese la cantidad de plata que se gasto en bebida: $'))
comida = float(input('Ingrese la cantidad de plata que se gasto en comida: $'))
alquiler = float(input('Ingrese la cantidad de plata que se gasto en el alquiler: $'))

a_pagar(personas,bebida,comida,alquiler)
