def sumaPrimUlt(lis):
    sumar = lis[0] + lis[-1]
    print(f'La suma de el primer y el ultimo número es: {sumar}')
    
def promedioPrimUlt(lis):
    promedio = (lis[0] + lis[-1] ) / 2
    print(f'El promedio de el primer y el ultimo número es: {promedio}')
    
lista = []
numero1 = float(input('Ingrese el primer numero a la lista: '))
lista.append(numero1)
numero2 = float(input('Ingrese el segudno número a la lista: '))
lista.append(numero2)
numero3 = float(input('Ingrese el tercer número a la lista: '))
lista.append(numero3)

lista_a_mostar = sumaPrimUlt(lista)

lista_a_mostar = promedioPrimUlt(lista)