
from flask import Flask, request

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "bienvenido a mi api"

@app.route("/saludo", methods=["POST"])
def saludo():
    data = request.json
    nombre = data.get("nombre", "Usuario")
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)