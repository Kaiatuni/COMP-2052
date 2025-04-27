from flask import Flask, render_template

app = Flask(__name__)

# Datos Dinámicos
libros = [
    {"id": 1, "nombre": "No tienes descuento the book", "precio": 69.99},
    {"id": 2, "nombre": "discount fighter 2 guide", "precio": 70.00}
]

usuarios = [
    {"id": 1, "nombre": "Ralph", "rol": "Usuario"},
    {"id": 2, "nombre": "Mario", "rol": "Usuario"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/libros")
def mostrar_productos():
    return render_template("libros.html", libros=libros)

@app.route("/usuarios")
def mostrar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)