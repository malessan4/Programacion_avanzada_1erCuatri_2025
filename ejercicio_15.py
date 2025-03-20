def calculo_dosis(dias_tratamiento, veces_por_dia, comprimidos_envase):
    dosis_total = dias_tratamiento * veces_por_dia
    if dosis_total > comprimidos_envase:
        return False
    else:
        return True
    
    
dias_tratamiento = int(input('Ingrese la cantidad de dias de tratamiento: '))
veces_por_dias = int(input('Ingrese la cantidad de veces por dia que debe tomar el remedio: '))
comprimidos_envase = int(input('Ingrese la cantidad de comprimidos que trae el envase: '))

tratamiento = calculo_dosis(dias_tratamiento,veces_por_dias,comprimidos_envase)

if tratamiento:
    print('El envase alcanza para el tratamiento completo')
else:
    print('El envase no alcanza para el tratamiento')
