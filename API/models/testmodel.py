import pickle
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.transform import resize
import numpy as np

# Images to be classified as:
Categories = [
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


test_model = pickle.load(open("/home/upijijis/Documentos/Github_clone/PymesHelper/API/models/Classification_Model.p","rb"))

# Testing for a new image
flat_data = []
url = input ('Enter url of image to test: ')
img_array = imread(url)
# Resize image
img_resized = resize(img_array,(150,150,3))
flat_data.append(img_resized.flatten())
flat_data = np.array(flat_data)
print("Dimensions of original image are:",img_array.shape)
plt.imshow(img_resized)
y_output = test_model.predict(flat_data)
y_output = Categories[y_output[0]]
# URLs to test:
#https://upload.wikimedia.org/wikipedia/commons/d/da/Strawberry_ice_cream_cone_%285076899310%29.jpg
#https://upload.wikimedia.org/wikipedia/commons/7/71/St._Bernard_puppy.jpg
#https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/1024px-Red_Apple.jpg
print("PREDICTED OUTPUT IS:",y_output)