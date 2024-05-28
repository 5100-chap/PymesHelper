import pickle
import numpy as np
import cv2


class ClassificationModel:
    def __init__(self, model_path):
        # Load the model from the file
        with open(model_path, "rb") as file:
            self.model = pickle.load(file)
        self.categories = [
            "FreshApple",
            "FreshBanana",
            "FreshGuava",
            "FreshJujube",
            "FreshOrange",
            "FreshPomegranate",
            "FreshStrawberry",
            "RottenApple",
            "RottenBanana",
            "RottenGuava",
            "RottenJujube",
            "RottenOrange",
            "RottenPomegranate",
            "RottenStrawberry",
        ]

    def classify(self, image):
        # Preprocess the image
        img = self.preprocess_image(image)

        # Perform classification using the model
        prediction = self.model.predict(img)

        # Get the predicted category
        predicted_category = self.categories[prediction[0]]

        return predicted_category

    def preprocess_image(self, image):
        # Resize the image to the required size (150x150)
        img_resized = cv2.resize(image, (150, 150))

        # Flatten the image data
        flat_data = img_resized.flatten()

        # Reshape the flattened data into a 2D array
        flat_data = flat_data.reshape(1, -1)

        return flat_data
