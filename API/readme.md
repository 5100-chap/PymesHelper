# API

Esta carpeta contiene todos los archivos y código relacionados con la API construida con Flask. La API es el backend del proyecto y se encarga de manejar las solicitudes y respuestas, interactuar con la base de datos y proporcionar los datos necesarios al frontend.

## Estructura

- Folders
    - [config](./config): Contiene los archivos de configuración de la API.
    - [models](./models): Contiene el manejo del modelo utilizados por la API.

- Files
    - [app.py](./app.py): Archivo principal de la aplicación Flask que define las rutas y la lógica de la API.
    - [varConfig.py](./config/varConfig.py): Archivo de configuración de variables.
    - [README.md](./README.md): Este archivo README.
## Requisitos

- Python 3.x
- Flask
- opencv-python
- numpy
- scikit-image
- matplotlib
- python-dotenv
- scikit-learn


## Instalación

1. Clona este repositorio.
2. Navega hasta la carpeta [API](../API).
3. Crea un entorno virtual de Python e instala las dependencias
4. Obtener el modelo, se puede usar de guia el notebook adentro de la carpeta [Entrenamiento](../Entrenamiento), y guardarlo en la carpera [models](./config/models) como Classification_Model.p
    1. Alternativamente, puede descargar el modelo que se uso a través de [este hipervinculo](https://www.mediafire.com/file/jijt66y8q6u82dj/Classification_Model.7z/file), si se opta por esta opcion debera de tener instalado el programa 7zip o similar, en caso de encontrarse en sistemas UNIX (Linux-MacOS), puede descomprimir [este archivo](https://www.mediafire.com/file/zr1sz68nsng5780/Classification_Model.tar.xz/file)

## Ejecución

Para ejecutar la API, sigue estos pasos:

1. Asegúrate de estar en la carpeta [API](../API).
2. Entre a la carpeta [config](./config/)
3. Asegure de actualizar el syslink de [models](./config/models) a la ruta absoluta en donde esta su carpeta [models](./models/)
   1. Alternativamente puede modificar la linea dentro del archivo [varConfig.py](./config/varConfig.py) 'MODEL_PATH = os.path.join(os.path.dirname(\_\_file\_\_), 'models', 'Classification_Model.p')' a 'MODEL_PATH = '/Direccion/Absoluta/hacia/el/modelo/Classification_Model.p''
4. Volver a la carpeta [raiz](../)
5. Ejecuta el siguiente comando: python .\API\app.py o python3 .\API\app.py 
