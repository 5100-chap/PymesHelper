import pickle
import numpy as np
import cv2

class ClassificationModel:
    def __init__(self, model_path):
        # Cargar el modelo desde el archivo
        with open(model_path, 'rb') as file:
            self.model = pickle.load(file)
    
    def classify(self, image):
        # Preprocesar la imagen
        img = self.preprocess_image(image)
        
        # Realizar la clasificación utilizando el modelo
        prediction = self.model.predict(img)
        
        # Devolver el resultado de la clasificación
        return prediction[0]
    
    def preprocess_image(self, image):
        # Leer la imagen utilizando OpenCV
        img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Redimensionar la imagen al tamaño requerido por el modelo
        img = cv2.resize(img, (224, 224))
        
        # Normalizar los valores de píxeles
        img = img / 255.0
        
        # Añadir una dimensión adicional para el batch
        img = np.expand_dims(img, axis=0)
        
        return img
