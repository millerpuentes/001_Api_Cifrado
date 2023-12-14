"""
Aqui se prueba el modulo de desencriptar un texto
"""
import os
import sys
import pytest
from cryptography.fernet import Fernet
PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)
from app.funciones.encriptado import desencriptando_texto

@pytest.mark.parametrize(
    "mensaje",
        [(b"a"),
        (b"A"),
        (b"mensaje"),
        (b"MeNsAjE"),
        (b"@"),
        (b"este es un mens@je"),
        (b"m3ns@j3 d3 pru3b4!!")
        ]
)
def test_desencriptando_texto(mensaje:str):
    """Funcion para probar la desencriptación

    Args:
        mensaje (str): Mensaje a ser encriptado y desencriptado con la funcion a probar
    """
    llave = Fernet.generate_key()
    entorno_cifrado = Fernet(llave)
    mensaje_encriptado = entorno_cifrado.encrypt(mensaje)
    mensaje_desencriptado = desencriptando_texto(mensaje_encriptado,llave)
    assert mensaje_desencriptado == mensaje
    