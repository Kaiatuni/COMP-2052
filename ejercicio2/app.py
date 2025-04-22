from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def principal():
    return "<h1>  Hola, este es el ejercicio 2, no hay descuento todavia. <h1>"

# ejercicio2 
usuarios = []


# Ruta GET para obtener información del servidor
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        'ejercicio': "2",
        'usuario': 'Kivan M. Lopez'
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.json

    nombre = data.get('nombre')
    correo = data.get('correo')
    
    if not nombre or not correo:
        return jsonify({
            'ERROR': 'Es debido tener ambos datos: nombre y correo'
        }), 400

    nuevo_usuario = {
        'id': len(usuarios) + 1,
        'nombre': nombre,
        'correo': correo,
    }

    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado exitosamente",
        "usuario": nuevo_usuario
    }), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

# Corrección final para ejecutar Flask
if __name__ == '__main__':  # ← aquí estaba el error: era __name__ y no name
    app.run(debug=True)