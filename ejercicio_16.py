def precio_con_iva(precio):
    iva = precio * 0.21 
    precio_con_iva = precio + iva
    print(f'El precio es ${precio} + el iva ${iva} es un precio final de ${precio_con_iva}')
    
precio_producto = float(input('Ingrese el precio de su producto: $'))

precio_con_iva(precio_producto)