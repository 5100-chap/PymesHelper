import pickle
import numpy as np
from skimage.transform import resize


class ClassificationModel:
    def __init__(self, model_path):
        # Cargar el modelo de clasificación
        with open(model_path, "rb") as file:
            self.model = pickle.load(file)
        self.categories = [
            "Manzana Fresca",
            "Platano Fresco",
            "Guayaba Fresca",
            "Azufaifa Fresca",
            "Naranja Fresca",
            "Granada Fresca",
            "Fresa Fresca",
            "Manzana Podrida",
            "Platano Podrido",
            "Guayaba Podrida",
            "Azufaifa Podrida",
            "Naranja Podrida",
            "Granada Podrida",
            "Fresa Podrida",
        ]

    def classify(self, image):
        # Preprocesa la imagen
        img = self.preprocess_image(image)

        # Realiza la predicción
        prediction = self.model.predict(img)

        # Consigue la prediccion
        predicted_category = self.categories[prediction[0]]

        return predicted_category

    def preprocess_image(self, image):
        # Redimensiona la imagen a 150x150
        img_resized = resize(image,(150,150,3))

        # Aplana los datos de la imagen
        flat_data = img_resized.flatten()

        # Redefine la forma de los datos
        flat_data = flat_data.reshape(1, -1)

        return flat_data
