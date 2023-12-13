"""
Este es el archivo principal
"""
from funciones.cifrado_cesar import cifrado_cesar

MENSAJE = "Hola mundo, estoy en un curso"
CLAVE = 2

resultado = cifrado_cesar(MENSAJE, CLAVE)
print(resultado)
