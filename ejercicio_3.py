def retorno_mensaje():
    return "Estudiando en la UNAB"

retorno_mensaje()



# para mostrar ese mensaje se deberia poner como
# el ejercicio anterior o 

mensaje = retorno_mensaje()
print(mensaje)

# tambien podria ser

print(retorno_mensaje())


# Punto C

def imprimir_mensaje(mensaje):
    print(mensaje)
    
imprimir_mensaje("Estudiando Matematica")

# otra forma

def retornoMensaje(mensaje):
    return mensaje

otro_mensaje = retornoMensaje("Estudiando Python en la UNAB")
print(otro_mensaje)