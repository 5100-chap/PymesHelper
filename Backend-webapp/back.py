from flask import Flask, request, jsonify
# from ..API.models.MLmodel import MLmodel

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
        if file.filename.split('.')[1] not in image_extensions:
            raise Exception(f"Debe utilizar un formato de imagen adecuado, los aceptados son: {image_extensions}")
        return f"Respuesta del modelo: work in progress..."
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__=="__main__":
    app.run(debug=True, threaded=True)