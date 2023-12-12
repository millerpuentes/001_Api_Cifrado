"""
Este es el archivo principal
"""
MENSAJE = "Hola mundo, estoy en un curso"
CLAVE = 2

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def cifrado_cesar(mensaje, clave):
    """Esta funcion genera un cifrado cesar a partir de un mensaje

    Args:
        mensaje(str): el mensaje a ser cifrado
        clave(int): clave de cifrado    
    
    """
    texto_cifrado=""

    for letra in mensaje.upper():
        if letra in ALFABETO:
            posicion = ALFABETO.index(letra)
            nueva_posicion = (posicion + clave) % len(ALFABETO)
            nueva_letra = ALFABETO[nueva_posicion]
            texto_cifrado += nueva_letra
        else:
            texto_cifrado += letra

    print("Texto Original: ", MENSAJE)
    print("Texto Cifrado: ", texto_cifrado)

print(cifrado_cesar("hola", 1))
