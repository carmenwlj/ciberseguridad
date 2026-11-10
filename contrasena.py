# PUK - Práctica Git y Github
contrasena = "carmen"
print(contrasena)

def comprobar_longitud(contrasena):
    return True if len(contrasena) >= 8 else False

def comprobar_mayuscula(contrasena):
    return True if any(char.isupper() for char in contrasena) else False

print(comprobar_longitud(contrasena))
print(comprobar_longitud("carmen1234"))

print(comprobar_mayuscula(contrasena))
print(comprobar_mayuscula("Carmen1234"))