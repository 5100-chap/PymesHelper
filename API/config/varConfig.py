from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env en el mismo directorio
load_dotenv()

# Configuración del modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'Classification_model.p')

# Configuración de SSL
SSL_CERT = os.environ.get('SSL_CERT')
SSL_KEY = os.environ.get('SSL_KEY')

# Otras configuraciones
HOST =  os.getenv('HOST')
PORT = int(os.getenv('PORT'))
DEBUG = 'True'
