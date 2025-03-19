def calculo_transporte(primero, segundo, tercero, colectivo):
    cantidad_primero = primero + 3
    cantidad_segundo = segundo + 3
    cantidad_tercero = tercero + 3
    cantidad_total = cantidad_primero + cantidad_segundo + cantidad_tercero
    cantidad_micros = cantidad_total / colectivo
    print(f'La cantidad de micros necesarios es {cantidad_micros}')
    
sala_primero = int(input('Ingrese la cantidad de alumnos de la 1er salita '))
sala_segundo = int(input('Ingrese la cantidad de alumnos de la 2da salita '))
sala_tercero = int(input('Ingrese la cantidad de alumnos de la 3er salita '))
asientos = int(input('Ingrese la cantidad de asientos que tiene el micro '))

calculo_transporte(sala_primero,sala_segundo,sala_tercero,asientos)
