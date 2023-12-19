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
