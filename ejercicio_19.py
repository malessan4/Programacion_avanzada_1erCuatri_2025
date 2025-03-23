class Dolar:
    def __init__(self, valor=0):
        self.valor = valor 

    def __str__(self):
        return 'USD$: ' + str(self.valor) 

    def convertirDolar(self): 
        cambio = self.valor * 1260
        print(f'El cambio de {self.valor} dolares es de ${cambio} pesos')

class Euro:
    def __init__(self, valor=0):
        self.valor = valor

    def __str__(self):
        return 'Euro$: ' + str(self.valor)
    
    def convertirEuro(self):
        cambio = self.valor * 1130
        print(f'El cambio de {self.valor} euros es de ${cambio} pesos')

class Real:
    def __init__(self, valor=0):
        self.valor = valor

    def __str__(self):
        return 'Real$: ' +  str(self.valor)
    
    def convertirReal(self):
        cambio = self.valor * 240
        print(f'El cambio de {self.valor} reales es de ${cambio} pesos')

moneda = Dolar(300)
print(moneda) 
moneda.convertirDolar()

moneda2 = Euro(400)
print(moneda2)
moneda2.convertirEuro()

moneda3 = Real(500)
print(moneda3)
moneda3.convertirReal()
