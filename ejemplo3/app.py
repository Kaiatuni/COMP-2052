from flask import Flask, request, jsonify

app = Flask(__name__)


todos = {"Todos": ["No","Tienes", "Descuento", "Skill Issue"] }

@app.route("/", methods=["GET"])
def home():
    return "simple TODO api"

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def insert_todos():
    data = request.json
    
    if not data or "todo" not in data:
        return jsonify({"error" : "Datos incompletos"})
    
    todos["Todos"].append(data['todo'])
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True)