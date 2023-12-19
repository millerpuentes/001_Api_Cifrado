"""Este es el modulo principal donde habrá la creacion y disposición de una API"""
from fastapi import FastAPI
from funciones.cifrado_cesar import cifrado_cesar
from funciones.encriptado import encriptando_texto
from funciones.hashing import text_hash

app = FastAPI()

@app.get("/")
def home():
    """
    Funcion principal de API
    """
    return {"Hola":"Mundo123"}

@app.get("/cifrado-cesar")
def url_cifrado_cesar(texto,clave):
    """
    URL para hacer encriptado CESAR
    Se debe ingresar el texto y la clave
    texto (str)
    clave (int)
    """
    salida = cifrado_cesar(texto,int(clave))
    return {"mensaje_cifrado":salida}

@app.get("/encriptado")
def url_encriptando_texto(mensaje,llave):
    """En esta url se podrá pedir la encriptación simetrica de un mensaje

    Args:
        mensaje (str): mensaje a ser encriptado
        llave (str): llave con la que se hará encriptación simetrica

    Returns:
        (json): respuesta de la api con mensaje encriptado
    """
    salida = encriptando_texto(mensaje.encode('utf-8'),llave.encode('utf-8'))
    return {"mensaje_encriptado":salida}

@app.get("/text_hash")
def url_text_hash(mensaje):
    """Url para hacer hashing de un mensaje con SHA256

    Args:
        mensaje (str): mensaje a ser hasheado
    """
    salida = text_hash(mensaje)
    return {"mensaje_hash": salida}
