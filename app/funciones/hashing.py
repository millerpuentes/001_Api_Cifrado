"""
Aqui se crea un modulo para obtener el hash de un string
"""
import hashlib

def text_hash(mensaje:str)->str:
    """
    Esta función devuelve el hash con el agoritmo sha256 a 32bytes

    Args:
        mensaje (str): mensaje a ser hasheado

    Returns:
        str: cadena de texto con el hash del mensaje
    """
    entorno_hash = hashlib.sha256()
    entorno_hash.update(mensaje.encode('utf-8'))
    salida = entorno_hash.hexdigest()
    return salida
