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
- Streamlit
- numpy
- python-dotenv
- opencv-python
- streamlit-webrtc
- av

## Instalación

1. Clona este repositorio.
2. Navega hasta la carpeta [Frontend-Webapp](../Frontend-Webapp).
3. Crea un entorno virtual de Python e instala las dependencias.

## Ejecución

Para ejecutar el frontend, sigue estos pasos:

1. Asegúrate de estar en la carpeta [Frontend-Webapp](../Frontend-Webapp).
2. Ejecuta el siguiente comando: streamlit run frontend.py