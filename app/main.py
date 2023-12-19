"""
Este es el archivo principal donde crea la API
"""
from fastapi import FastAPI
from funciones.cifrado_cesar import cifrado_cesar
app =FastAPI()

@app.get("/")
def home():
    """
    Función prinipal del API
    """
    return{"Hola":"Mundo123"}

@app.get("/cifrado-cesar")
def url_cifrado_cesar(texto:str,clave:int)->str:
    """
    URL para hacer encriptado CESAR
    Se debe ingresar el texto y la clave
    texto (str)
    clave (int)
    """
    salida = cifrado_cesar(texto, int(clave))
    return {"mensaje_cifrado ":salida}
