def comprobar_numero(contrasena):
    return True if any(char.isdigit() for char in contrasena) else False