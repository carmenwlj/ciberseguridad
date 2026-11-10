# PUK - Práctica Git y Github
from utilidades import comprobar_numero

contrasena = "carmen"
print(contrasena)

def comprobar_longitud(contrasena):
    return True if len(contrasena) >= 8 else False

print(comprobar_longitud(contrasena))
print(comprobar_longitud("carmen1234"))
print(comprobar_numero(contrasena))
print(comprobar_numero("carmen1234"))