"""Aqui se colocan los test para el archivo main.py"""
import sys
import os
from fastapi.testclient import TestClient

# pylint: disable=C0413
sys.path.append(os.path.dirname(os.path.dirname("app/funciones/")))
from app.main import app

client = TestClient(app)


def test_url_cifrado_cesar():
    """
    Prueba unitaria para verificar api con cifrado cesar
    """
    respuesta = client.get("/cifrado-cesar?texto=hello&clave=3")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"mensaje_cifrado": "KHÑÑR"}


def test_url_encriptando_texto():
    """Prueba unitaria para encriptación de texto"""
    respuesta = client.get(
        "/encriptado?mensaje=hola&llave=UyJ4iWnYDPOcZ3sCmwNZtKbIudZRYl5n7owVTiQ4r3o="
    )
    assert respuesta.status_code == 200

def test_text_hash():
    """Esta es la prueba unitaria del modulo de hashing"""
    respuesta = client.get("/text_hash?mensaje=Hola")
    esperado = "e633f4fc79badea1dc5db970cf397c8248bac47cc3acf9915ba60b5d76b0e88f"
    assert respuesta.status_code == 200
    assert respuesta.json() == {"mensaje_hash": esperado}
    