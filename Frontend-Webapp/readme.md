# Frontend-Webapp

Esta carpeta contiene todos los archivos y código relacionados con el frontend de la aplicación web. El frontend está construido con Streamlit y utiliza las bibliotecas OpenCV y Streamlit-webrtc para el procesamiento de imágenes y la transmisión en tiempo real.

## Estructura

- Folders
    - [Camera](./Camera): Contiene los archivos relacionados con la lógica de la cámara.

- Files
    - [frontend.py](./frontend.py): Archivo principal de la aplicación frontend que define la interfaz de usuario y la lógica de la aplicación.
    - [README.md](./README.md): Este archivo README.

## Requisitos

- Python 3.x
- streamlit
- numpy
- python-dotenv
- opencv-python
- streamlit-webrtc
- av

## Instalación

1. Clona este repositorio.
3. Crea un entorno virtual de Python e instala las dependencias.

## Ejecución

Para ejecutar el frontend, sigue estos pasos:

1. Asegúrate de estar en la carpeta [raiz](../).
2. Ejecuta el siguiente comando: streamlit run ./Frontend-Webapp/frontend.py

## Recomendaciones
Se recomienda que para evitar algun tipo de problemas se corra la pagina con HTTPS, aqui una forma de hacerlo
1. En la carpeta [raiz](../) crea la carpeta .streamlit
2. Agregue un archivo llamado config.toml en donde se tenga lo siguiente:

[server]
headless = true
enableCORS = true
port = 8501
sslCertFile = "path/to/certificate.crt"
sslKeyFile = "path/to/privatekey.key"

[browser]
serverAddress = "127.0.0.1"
serverPort = 8501

Puede configurar los puertos y la dirección del servidor acorde a lo que se requiera

3. Siga los pasos de ejecución, con ello la pagina debería de correr en HTTPS

