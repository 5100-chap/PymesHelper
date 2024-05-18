from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def peticion():
    return "<span>HOLA</span>"

@app.route("/file", methods=["POST"])
def send_file():
    file = request.files["file"]
    print(f"The name of the file: {file.filename}")
    return f"<span>Petición mandada!!</span><br><span style='blue;'>{file.filename}</span>"

if __name__=="__main__":
    app.run(debug=True, threaded=True)