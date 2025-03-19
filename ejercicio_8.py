def calculo_rebaja(precio_anterior, precio_rebaja):
    descuento = precio_anterior - precio_rebaja
    porcentaje = (descuento / precio_anterior) * 100
    print(f'El descuento es de {porcentaje}% ')
    
precio_anterior = int(input("Ingrese el precio anterior "))
precio_rebaja = int(input("Ingrese el precio de rebaja "))
calculo_rebaja(precio_anterior, precio_rebaja)