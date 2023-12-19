# Api De Cifrado y Encriptado

## Descripción

Este proyecto es una api que permite cifrar y encriptar mensajes, para ello se utilizan los algoritmos de cifrado, encriptado y hashing

## Instalación

Para instalar el proyecto se debe clonar el repositorio.
1. Crear un ambiente virtual (compatible con python 3.8, 3.9 y 3.10)
```bash
python -m venv venv
```
2. Activar el ambiente virtual

* Linux:
```bash
source venv/bin/activate
```

* Windows:
```bash
venv\Scripts\activate.bat
```

3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

4. Ingresar a la carpeta app
```bash
cd app
```

5. Correr aplicación con un servidor como uvicorn desde la carpeta app
```bash
uvicorn main:app --reload
```

6. Ingresar a la url http://localhost:8000/docs para ver la documentación de la api

## Uso

Para utilizar la api se debe ingresar a la url http://localhost:8000/docs y probar los endpoints

Existen 4 endpoints:
* `/` : Enpoint de inicio o home
* `/cifrado-cesar`: Endpoint para cifrar un mensaje con el algoritmo de cifrado cesar
* `/encriptado`: Endpoint para encriptar un mensaje con el algoritmo de encriptacion simetrica
* `/text_hash`: Endpoint para generar un hash de un mensaje con el algoritmo de hashing Sha256.

## Descripcion técnica

### Estructura del proyecto
```
.
├── .github/
│   └── worflows/
│       └── verificacion.yml
├── app/
│   ├── funciones/
│   │   ├── cifrado_cesar.py
│   │   ├── encriptado.py
│   │   └── hashing.py
│   └── main.py
├── img/
├── tests/
│   ├── test_cifrado_cesar.py
│   ├── test_desencriptando_texto.py
│   ├── test_encriptando_texto.py
│   ├── test_main.py
│   └── test_text_hash.py
├── .gitignore
├── .pylintrc
├── README.md
└── requirements.txt
```
### configuraciones

No requiere configuraciones adicionales a los pasos expuestos en la sección de instalación

### Modulo de pruebas

Para ejecutar las pruebas se debe ejecutar el siguiente comando
```bash
pytest --cov=app tests/
```
