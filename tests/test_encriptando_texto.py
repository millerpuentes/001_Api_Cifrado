"""
Aqui se prueba la función de encriptado simétrico
"""
import os
import sys
import pytest
from cryptography.fernet import Fernet

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from app.funciones.encriptado import encriptando_texto

@pytest.mark.parametrize(
        "mensaje,llave",
        [
        (
        b"a",
        b"UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
        ),

        (
        b"b",
        b"UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
        ),

        (
        b"Este es mi curso de python",
        b"UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
        )
        ])
def test_encriptando_texto(mensaje:str,llave:str):
    """ funcion para probar la encriptacion de textos

    Args:
        mensaje (str): Mensaje a ser encriptado
        llave (str): llave de encriptacion simetrica
    """
    entorno_cifrado = Fernet(llave)
    salida = encriptando_texto(mensaje,llave)
    mensaje_desencriptado = entorno_cifrado.decrypt(salida)
    assert mensaje_desencriptado == mensaje
    