def armo_cartel(producto, precio_anterior, precio_rebaja):
    print(f'*************************************')
    print(f'Atención!!! Gran rebaja para el producto {producto} ')
    print(f'Antes: ${precio_anterior}')
    print(f'Ahora: ${precio_rebaja}')
    
producto = input('Ingrese el nombre del producto: ')
precio_anterior = int(input('Ingrese el precio anterior del producto $'))
precio_rebaja = int(input('Ingrese el precio con la rebaja $'))

armo_cartel(producto,precio_anterior,precio_rebaja)