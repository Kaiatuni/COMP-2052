from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="<tu-contraseña>",  # Reemplaza con tu contraseña real
    database="test_db"
)
cursor = db.cursor(dictionary=True)  # Para que los resultados sean dicts

# Crear datos
@app.route('/create', methods=['POST'])
def create_user():
    data = request.json
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (data['name'], data['email'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Usuario creado"}), 201

# Leer datos
@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

# Actualizar datos
@app.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    values = (data['name'], data['email'], id)
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Usuario actualizado"})

# Eliminar datos
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (id,))
    db.commit()
    return jsonify({"message": "Usuario eliminado"})

if __name__ == "__main__":
    app.run(debug=True)