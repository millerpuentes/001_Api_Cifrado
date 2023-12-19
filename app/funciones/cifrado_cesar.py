"""
Este modulo hace un cifrado cesar
"""

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrado_cesar(mensaje:str, clave:int)->str:
    """Esta funcion genera un cifrado cesar a partir de un mensaje

    Args:
        mensaje(str): el mensaje a ser cifrado
        clave(int): clave de cifrado   
    
    return:
        texto_cifrado (str): el texto ya cifrado 
    
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

    return texto_cifrado
