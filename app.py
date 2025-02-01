from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Simulación de JSON de datos
data = {"message": "Hola desde Railway con Python"}

@app.route("/")
def home():
    return "Bienvenido a mi API en Railway"

@app.route("/json")
def get_json():
    return jsonify(data)

@app.route("/set-cookie")
def set_cookie():
    resp = make_response(jsonify({"message": "Cookie establecida"}))
    resp.set_cookie("mi_cookie", "valor_cookie", max_age=60*60*24)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
