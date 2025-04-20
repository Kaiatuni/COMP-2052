from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'nombre': 'Mi Aplicación Flask',
        'versión': '1.0',
        'descripción': 'Este es un servidor Flask de ejemplo con dos rutas.'
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    if not data or 'mensaje' not in data:
        return jsonify({'error': 'Se requiere un campo "mensaje" en formato JSON.'}), 400

    mensaje_usuario = data['mensaje']
    respuesta = f"Recibí tu mensaje: '{mensaje_usuario}'. ¡Gracias por enviarlo!"

    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)