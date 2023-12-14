"""
Este modulo comprueba que se haga un buen hashing de los textos
"""
import os
import sys
import pytest
from app.funciones.hashing import text_hash

PROJECT_ROOT = os.path.abspath(os.path.join(
               os.path.dirname(__file__),
               os.pardir))
sys.path.append(PROJECT_ROOT)

@pytest.mark.parametrize(
    "mensaje,hash_esperado",
    [
        ("Hola", "e633f4fc79badea1dc5db970cf397c8248bac47cc3acf9915ba60b5d76b0e88f"),
        ("A", "559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd"),
        ("a", "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"),
        ("1", "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b"),
        ("A1b2", "2f8c6f88e15bba2d53d753346784a3f2fcba4472a078c08788072c68ecf3307d"),
        (
            "Este es un mensaje aleatorio",
            "5634339f53a8a1a83f86fc1a9d5d013515c4c7cb761752b31a6287038d62d59e",
        ),
        (
            "Mi clave es: 123@",
            "ac8d836ccfa8f549bced5792c73e8255d6ea74358e916e7e0fd6c2c7c582777c",
        ),
    ],
)
def test_text_hash(mensaje:str,hash_esperado:str):
    """Funcion para probar el hashing de texto

    Args:
        mensaje (str): Mensaje a ser hasheado
        hash (str): el hash correspondiente al mensaje
    """
    esperado_sha256 = hash_esperado
    salida = text_hash(mensaje=mensaje)
    assert salida == esperado_sha256
