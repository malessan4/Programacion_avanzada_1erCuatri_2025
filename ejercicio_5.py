def cuantos_dias (mes):
    if mes == 1:
        print(31)
        
    elif mes == 2:
        print(28)
        
    elif mes == 3:
        print(31)
        
    elif mes == 4:
        print(30)

    elif mes == 5:
        print(31)
        
    elif mes == 6:
        print(30)
        
    elif mes == 7:
        print(31)
        
    elif mes == 8:
        print(31)
        
    elif mes == 9:
        print(30)
        
    elif mes == 10:
        print(31)
        
    elif mes == 11:
        print(30)
        
    elif mes == 12:
        print(31)

    else:
        print("INGRESE UN NÚMERO VALIDO")
        
numero_mes = int(input("Ingrese el número de mes "))

cuantos_dias(numero_mes)

