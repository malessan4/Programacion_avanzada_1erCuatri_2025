# Se crea el objeto Fraccion 
class Fraccion:
    def __init__(self, a=0, b=1):
        self.fracciones = [a, b]
        

    def cargarFraccion(self):
        a = int(input('Ingrese el valor del NUMERADOR: '))
        b = int(input('Ingrese el valor del DENOMINADOR: '))
        self.fracciones[0] = a
        self.fracciones[1] = b

    def numerador(self):
        return self.fracciones[0]

    def denominador(self):
        return self.fracciones[1]

    def __str__(self):
        return str(self.fracciones[0]) + '/' + str(self.fracciones[1])



# SUMA
    def sumaFracciones(self, otra_fraccion):
        num1 = self.numerador()
        den1 = self.denominador()
        num2 = otra_fraccion.numerador()
        den2 = otra_fraccion.denominador()
        if den1 == den2:
            nuevo_numerador = num1 + num2
            mismo_denominador = den1
            print(f'La suma de las fracciones da: {nuevo_numerador}/{mismo_denominador}')
            return Fraccion(nuevo_numerador, mismo_denominador)

        else:
            nuevo_numerador = (num1 * den2) + (num2 * den1)
            nuevo_denominador = den1 * den2

            print(f'La suma de las fracciones da: {nuevo_numerador}/{nuevo_denominador}')
            return Fraccion(nuevo_numerador, nuevo_denominador)


# RESTA
    def restaFracciones(self, otra_fraccion):
        num1 = self.numerador()
        den1 = self.denominador()
        num2 = otra_fraccion.numerador()
        den2 = otra_fraccion.denominador()
        if den1 == den2:
            nuevo_numerador = num1 - num2
            mismo_denominador = den1
            print(f'La resta de las fracciones da: {nuevo_numerador}/{mismo_denominador}')
            return Fraccion(nuevo_numerador, mismo_denominador)
        else:
            nuevo_numerador = (num1 * den2) - (num2 * den1)
            nuevo_denominador = den1 * den2
            print(f'La resta de las fracciones da: {nuevo_numerador}/{nuevo_denominador}')
            return Fraccion(nuevo_numerador, nuevo_denominador)


# MULTIPLICACION

    def multiFracciones(self, otra_fraccion):
        num1 = self.numerador()
        den1 = self.denominador()
        num2 = otra_fraccion.numerador()
        den2 = otra_fraccion.denominador()
        nuevo_numerador = num1 * num2
        nuevo_denominador = den1 * den2
        print(f'La multiplicacion de las fracciones da: {nuevo_numerador}/{nuevo_denominador}')
        return Fraccion(nuevo_numerador, nuevo_denominador)

# DIVISION

    def diviFracciones(self, otra_fraccion):
        num1 = self.numerador()
        den1 = self.denominador()
        num2 = otra_fraccion.numerador()
        den2 = otra_fraccion.denominador()
        if den1 == den2:
            nuevo_numerador = num1 * num2
            nuevo_denominador = num2 * den1
            print(f'La division de las fracciones da: {nuevo_numerador}/{nuevo_denominador}')
            return Fraccion(nuevo_numerador, nuevo_denominador)
        else:
            nuevo_numerador = num1 * den2
            nuevo_denominador = num2 * den1
            print(f'La division de las fracciones da: {nuevo_numerador}/{nuevo_denominador}')
            return Fraccion(nuevo_numerador, nuevo_denominador)

print("Bienvenidos/as a cuentas con Fracciones")
fracA = Fraccion ()
fracA.cargarFraccion()
print(fracA)
fracB = Fraccion ()
fracB.cargarFraccion()
print(fracB)
suma = fracA.sumaFracciones(fracB)
resta = fracA.restaFracciones(fracB)
multi = fracA.multiFracciones(fracB)
divi = fracA.diviFracciones(fracB)

