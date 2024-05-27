# app.py
from flask import Flask, request, jsonify
from models.MLmodel import ClassificationModel
from config import varConfig
import base64
import cv2
import numpy as np

app = Flask(__name__)

# Cargar el modelo de clasificación
classification_model = ClassificationModel(varConfig.MODEL_PATH)

@app.route('/classify', methods=['POST'])
def classify_image():
    try:
        # Obtener la imagen del request
        image = request.files['image']
        
        # Realizar la clasificación utilizando el modelo
        result = classification_model.classify(image)
        
        # Devolver el resultado como respuesta JSON
        return jsonify({'classification': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/classify_video', methods=['POST'])
def classify_video():
    try:
        # Obtener el video del request
        video_data = request.get_data()
        
        # Decodificar el video de base64
        video_bytes = base64.b64decode(video_data)
        
        # Leer el video con OpenCV
        video = cv2.imdecode(np.frombuffer(video_bytes, np.uint8), cv2.IMREAD_COLOR)
        
        # Realizar la clasificación utilizando el modelo
        result = classification_model.classify(video)
        
        # Devolver el resultado como respuesta JSON
        return jsonify({'classification': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# Configuración de SSL
ssl_context = (varConfig.SSL_CERT, varConfig.SSL_CERT)


if __name__ == '__main__':
    app.run(debug=varConfig.DEBUG, host=varConfig.HOST, port=varConfig.PORT)
