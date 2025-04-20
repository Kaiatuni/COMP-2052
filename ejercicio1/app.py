from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'nombre': 'Ejercicio1 de flask',
        'versión': '1.0',
        'descripción': 'Intento de hacer los ejercicios porque algunos no corren'
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    if not data or 'mensaje' not in data:
        return jsonify({'error': 'Se requiere un campo "mensaje" en formato JSON.'}), 400

    mensaje_usuario = data['mensaje']
    respuesta = f"'{mensaje_usuario}'"

    return jsonify({'Aqui tienes tu respuesta:': respuesta})

if __name__ == '__main__':
    app.run(debug=True)
    #no se que hice pero esto me corre mientras que los ejemplos no me corren :(
        #me deje llevar por ejercicios de otros y cuando puse http en vez de .rest me corrio 