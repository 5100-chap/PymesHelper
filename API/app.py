from flask import Flask, request, jsonify
from models.MLmodel import MLmodel
import base64
import numpy as np
import cv2

app = Flask(__name__)

image_extensions = ['jpg', 'jpeg', 'png', 'svg']

@app.route("/", methods=["GET"])
def peticion():
    return "<span>HOLA</span>"

@app.route("/file", methods=["POST"])
def send_file():
    try:
        file = request.files["file"]
        # print(f"The name of the file: {file.filename}")
        # print(f"{file.filename.split('.')[1]}")
        if file.filename.split('.')[-1] not in image_extensions:
            raise Exception(f"Debe utilizar un formato de imagen adecuado, los aceptados son: {image_extensions}")
        # Decodificacion de la imagen
        image_data = base64.b64decode(file.stream().read())
        matrix = np.frombuffer(image_data, dtype=np.uint8)
        img = cv2.imdecode(matrix, cv2.IMREAD_COLOR)

        processed_image, results = MLmodel.process_image(image=img)

        return jsonify({"image": processed_image, "result": results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__=="__main__":
    app.run(debug=True, threaded=True)