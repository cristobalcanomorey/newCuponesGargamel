from flask import Flask, render_template, redirect, url_for, request, make_response
from datetime import datetime
from urllib.parse import quote, unquote
import json  # Importar el módulo json

app = Flask(__name__)

# Simulación de una base de datos de cupones
coupons = {
    "2025-01-31": {
        "code": "CUPON0",
        "titulo": "Cupon 0",
        "description": "Descuento del 10%",
        "rules":"Reglas del cupon",
        "img":"https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif",
        "date":"2025-01-31"
        },
    "2025-02-01": {
        "code": "CUPON1",
        "titulo": "Te deseo mucha suerte",
        "description": """🍀🍀Te deseo que tengas muchísima suerte en el examen de catalán!! 🍀🍀

Lo hablas muy bien para lo poco que llevas aprendiendo, se te dan realmente bien los idiomas. 👌

Yo creo que tienes posibilidades, tú confía en ti y dale caña 💪""",
        "rules": "Reglas del cupon",
        "img": 'static/img/gargamelSuerte.jpeg',
        "date": "2025-02-01"
        },
    "2025-02-02": {
        "code": "CUPON2",
        "titulo": "Cupon 2",
        "description": "Descuento del 10%",
        "rules": "Reglas del cupon",
        "img": "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif", 
        "date": "2025-02-02"
        },
}

# Lista para almacenar los cupones desbloqueados
unlocked_coupons = []

@app.route('/')
def index():
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Leer y decodificar la cookie
    unlocked_dates_cookie = request.cookies.get('unlocked_coupons', '')
    unlocked_dates = unquote(unlocked_dates_cookie).split(",") if unlocked_dates_cookie else []
    
    # Cargar los cupones desbloqueados basados en las fechas
    unlocked_coupons.clear()  # Limpiar la lista actual
    for date in unlocked_dates:
        if date:  # Ignorar cadenas vacías
            # Buscar el cupón por su fecha
            if date in coupons:
                coupon = coupons[date]
                if coupon not in unlocked_coupons:
                    unlocked_coupons.append(coupon)
    print( unlocked_coupons )
    if today in coupons:
        coupon = coupons[today]
        if coupon in unlocked_coupons:
            # Si el cupón del día ya está desbloqueado, redirigir a la lista de cupones
            return redirect(url_for('coupon_list'))
        else:
            # Si no está desbloqueado, mostrar el GIF
            return render_template('index.html', today=today, coupon=coupon)
    else:
        return "No hay cupones disponibles hoy."

from flask import jsonify

@app.route('/unlock/<date>')
def unlock_coupon(date):
    if date in coupons:
        coupon = coupons[date]
        
        # Leer y decodificar la cookie existente
        unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
        unlocked_coupons = json.loads(unlocked_coupons_cookie)
        
        # Si el cupón no está en la lista, agregarlo
        if date not in unlocked_coupons:
            unlocked_coupons[date] = {"code": coupon["code"], "description": coupon["description"], "redeemed": False}
        
        # Guardar la cookie actualizada
        response = make_response(jsonify(coupon))  # Devolver el cupón en formato JSON
        response.set_cookie('unlocked_coupons', json.dumps(unlocked_coupons))  # Convertir el diccionario en una cadena JSON
        return response
    else:
        return jsonify({"error": "Cupón no disponible."}), 404

@app.route('/redeem/<code>')
def redeem_coupon(code):
    # Leer y decodificar la cookie
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    unlocked_coupons = json.loads(unlocked_coupons_cookie)
    
    # Buscar el cupón por su código
    for date, coupon in unlocked_coupons.items():
        if coupon["code"] == code:
            # Marcar el cupón como canjeado
            coupon["redeemed"] = True
            # Guardar la cookie actualizada
            response = make_response(jsonify({"status": "success", "message": "Cupón canjeado correctamente."}))
            response.set_cookie('unlocked_coupons', json.dumps(unlocked_coupons))
            return response
    
    return jsonify({"status": "error", "message": "Cupón no encontrado."}), 404

@app.route('/unlocked/<code>')
def unlocked_coupon(code):
    coupon = next((c for c in unlocked_coupons if c['code'] == code), None)
    if coupon:
        return render_template('unlocked_coupon.html', coupon=coupon)
    else:
        return "Cupón no encontrado."

@app.route('/coupons')
def coupon_list():
    # Leer y decodificar la cookie
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    unlocked_coupons = json.loads(unlocked_coupons_cookie)
    
    # Convertir el diccionario en una lista para la plantilla
    coupons_list = [coupon for coupon in unlocked_coupons.values()]
    return render_template('coupon_list.html', coupons=coupons_list)

@app.route('/coupon/<code>')
def coupon_detail(code):
    # Leer y decodificar la cookie
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    unlocked_coupons = json.loads(unlocked_coupons_cookie)
    
    # Buscar el cupón por su código
    coupon = next((coupon for coupon in unlocked_coupons.values() if coupon["code"] == code), None)
    if coupon:
        return render_template('unlocked_coupon.html', coupon=coupon)
    else:
        return "Cupón no encontrado."

if __name__ == '__main__':
    app.run(debug=True)