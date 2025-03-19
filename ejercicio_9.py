def calculo_nuevo_precio(precio_anterior, porcentaje):
    porcentaje_decimal = porcentaje / 100 
    monto_aumento = precio_anterior * porcentaje_decimal
    precio_aumentado = precio_anterior + monto_aumento
    print(f'El precio final es de ${precio_aumentado}')
    
precio_anterior = int(input('Ingrese el precio actual del producto $'))
porcentaje = int(input('Ingrese el porcentaje que quiere aumentar al precio %'))
calculo_nuevo_precio(precio_anterior,porcentaje)