"""
Este modulo trabajará una encriptación simétrica
"""
from cryptography.fernet import Fernet

def encriptando_texto(mensaje:str, llave:str)->str:
    """
    Esta funcion hace un encriptado simétrico

    Args:
        mensaje(str): el mensaje a ser encriptado
        llave(int): es la llave de encriptación
    
    return:
        (str): Mensaje encriptado 
    
    """
    #llave = Fernet.generate_key()
    entorno_cifrado = Fernet(llave)
    mensaje_encriptado = entorno_cifrado.encrypt(mensaje)

    return mensaje_encriptado

def desencriptando_texto(mensaje_encriptado:str,llave:str)->str:
    """funcion para desencriptar mensaje con una llave

    Args:
        mensaje_encriptado (str): mensaje raro, listo para ser traducido a un lenguaje mas comun
        llave (str): llave de encruptacion/desencriptación

    Returns:
        str: mensaje desencriptado
    """
    entorno_cifrado = Fernet(llave)
    mensaje_desencriptado = entorno_cifrado.decrypt(mensaje_encriptado)
    return mensaje_desencriptado
