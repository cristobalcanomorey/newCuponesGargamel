from flask import Flask, render_template, redirect, url_for, request, make_response
from datetime import datetime
from urllib.parse import quote, unquote
import json  # Importar el módulo json

app = Flask(__name__)

# Simulación de una base de datos de cupones
coupons = {
    # "2025-02-01": {
    #     "code": "CUPON1",
    #     "mensaje_desbloqueo": "¡Cupón Desbloqueado!",
    #     "titulo": "Te deseo mucha suerte",
    #     "description": """🍀🍀Te deseo que tengas muchísima suerte en el examen de catalán!! 🍀🍀 Lo hablas muy bien para lo poco que llevas aprendiendo, se te dan realmente bien los idiomas. 👌 Yo creo que tienes posibilidades, tú confía en ti y dale caña 💪""",
    #     "activado": False,
    #     "canjeable": False,
    #     "serio": False,
    #     "rules": "Reglas del cupon",
    #     "img": 'static/img/gargamelSuerte.jpeg',
    #     "date": "2025-02-01"
    #     },
    # "2025-02-01": {
    #     "code": "CUPON2",
    #     "mensaje_desbloqueo": "",
    #     "titulo": "Necesito un poco de espacio",
    #     "description": "Entiendo que estás pasando por un mal momento y siento muchísimo no haber respetado tus sentimientos y haber resultado ser una carga más éstos días. Si decides activar el cupón te doy el espacio que necesites, prometo respetar tu decisión y no intentaré hacer nada para recuperar nuestra amistad mientras el cupón esté activo. Independientemente de eso siempre que quieras contarme algo, si quieres un táper o si quieres que te ayude con lo que sea quiero que sepas que siempre puedes contar conmigo. Ah y cuando termine de instalarme las puertas de mi casa siempre estarán abiertas para ti, si me avisas con tiempo igual te invito a unas croquetas recién hechas y tal.",
    #     "canjeable": True,
    #     "serio": True,
    #     "rules": "Puedes activarlo tantas veces como quieras",
    #     "toggle": True,
    #     "activado": False,
    #     "img": "static/img/gargamelSerio.jpe", 
    #     "date": "2025-02-02"
    #     },
    "2025-02-02": {
        "code": "CUPON2",
        "mensaje_desbloqueo": "",
        "titulo": "Chapa",
        "description": """Hola Rocío... cómo te encuentras? Espero que te encuentres mejor.
Teniendo en cuenta lo mal que lo estás pasando ahora y lo egoísta que he sido, dudo mucho que vayas a entrar hoy en ésta gilipollez de página web. Si por casualidad estás leyendo ésto, muchas gracias por todo. Nunca podré compensarte lo suficiente por todo lo que me has enseñado y todo lo que has aportado a mi felicidad, grácias a ti me dí cuenta de que sin querer estaba siendo una carga para mis padres por no hacerme cargo yo de mis propias responsabilidades, desde entonces he estado trabajando en intentar dejar de ser una carga para ellos, trabajo el cual ha culminado hoy en mi emancipación. 

También me has otorgado la oportunidad de descubrir que puedo aportar a la felicidad de los demás. Sé que es algo de sentido común pero yo realmente creía que mi existencia era superflua, que de alguna forma ni yo podía aportar nada en ésta vida ni la vida podía aportarme nada a mí. Al ver que podía aportar un poquito a vuestra felicidad me he dado cuenta de que sí existo. Ésa ha sido siempre la razón por la que he hecho cosas por vosotras, mi miedo a volver a desaparecer y mis ganas de aportar todo lo posible para así poder decir que he sido capaz de aportar algo positivo en ésta vida antes de pasar a la siguiente y que no he existido sólo para gastar oxígeno.

He estado reflexionando mucho y creo que tenías razón cuando dijiste que tal vez he estado confundiendo mis sentimientos… nunca antes me había sentido tan unido a nadie y nunca nadie me había aportado tanto en cuanto a crecimiento personal y autoconocimiento. Contigo he sentido que existo, tú estando tan involucrada en tu vida y siendo el centro y los cimientos de todo tu mundo y el de Itziar, en contraste conmigo que he estado viviendo siempre en una burbuja de cristal y al márgen de todo, siendo un mero espectador de una vida en la que ni pincho ni corto. Creo que sentía que para mí ya era demasiado tarde para vivir mi propia vida y posiblemente de alguna forma intentaba vivir a través de ti. Sentía que a pesar de no poder aportar a mi propia vida nada de valor tal vez sí podría aportar algo de valor a la vuestra…

Creo que ésa es la razón por la que tenía tanto miedo a perderte, por eso pensaba a todas horas en ti, en tus problemas y en qué podría hacer para aportar, por eso siento tanta admiración hacia ti, por eso pensé que sólo en una relación podría aportar lo máximo posible y por eso lo confundí con amor…

Creo que debería serte sincero, a pesar de decir que priorizaba nuestra amistad a ésa emoción la verdad es que ésa emoción tan intensa de anhelo por formar parte de la vida que estaba confundiendo con el amor no ha sido fácil de sobrellevar… En algunas ocasiones lo he pasado bastante mal la verdad, por patético que pueda sonar también he llegado a sentir incluso celos… No es ni medio normal, lo sé… Tenía miedo a que te marchases de mi vida y que te la llevases contigo ahora que había empezado a vivirla

Pero ahora que tengo mi primer trabajo de lo que me apasiona y mi propia casa siento que tal vez, al fin y al cabo, no era demasiado tarde para mí. Tal vez yo nunca llegue a poder vivir la vida plenamente ni tenga hijos y sé que seguramente me quede algo de tara por el retraso en mi desarrollo y mi madurez, sé que me dejaré muchas cosas por vivir porque he procrastinado mucho y me he puesto a ello muy tarde… Pero aun así ahora empiezo a entender que puedo vivir mi propia vida y que no está todo perdido ni tengo que vivir indirectamente a través de nadie. Estoy entusiasmado por ello y me haría mucha ilusión que tú estuvieras a mi lado en éste proceso, me gustaría mucho que vinieses conmigo a hacer una compra grande en el súper o al Ikea a comprar unas cosillas que necesito. Me gustaría invitarte a mi casa algún día e invitarte a unas croquetas recién fritas o a un ramen…

Sé que últimamente tendemos a distanciarnos cada vez más, tal vez se esté aproximando el momento en que nuestros caminos se separan. Tarde o temprano tenía que pasar… Realmente espero que éste distanciamiento sea temporal y volvamos a unirnos más pero de no ser el caso de lo único de lo que me arrepentiré, a parte de haber roto tu confianza y haberte hecho daño por supuesto, será de no haber valorado lo que tenía y de no haber podido darme cuenta antes de lo que sentía realmente. Por lo menos he llegado a darme cuenta a pesar de haberlo hecho tarde, cuando ya había permitido que se interpusiera entre nosotros y después de haberte faltado al respeto y traicionado tu confianza.

Siempre te estaré eternamente agradecido por haberme enseñado todo lo que me has enseñado directa e indirectamente, por tu comprensión, tu apoyo, por haber creído en mí en algún momento y sobre todo por tu mano dura, que realmente me hacía falta para espabilar…

Te quiero mucho Rocío, siempre te he querido aunque no haya sabido lo que ello significaba hasta ahora. 

        """,
        "canjeable": True,
        "serio": True,
        "rules": "Puedes activarlo tantas veces como quieras",
        "toggle": True,
        "activado": False,
        "img": "static/img/gargamelSerio.jpe", 
        "date": "2025-02-02"
        },
    # "2025-02-02": {
    #     "code": "CUPON2",
    #     "titulo": "Espacio",
    #     "description": "Entiendo que estás pasando por un mal momento y siento muchísimo no haber respetado tus sentimientos y haber resultado ser una carga más. Una vez activado el cupón te doy el espacio que necesites, prometo respetar tu decisión y no intentar hacer nada para recuperar nuestra amistad mientras el cupón esté activo. Independientemente de eso siempre que quieras contarme algo, si quieres comida o si quieres que te ayude con lo que sea quiero que sepas que siempre puedes contar conmigo.",
    #     "rules": "Puedes activarlo tantas veces como quieras",
    #     "activado": False,
    #     "img": "static/img/gargamelSerio.jpeg", 
    #     "date": "2025-02-02"
    #     },
    "2025-02-03": {
        "code": "CUPON3",
        "titulo": "Suministro de galletas",
        "description": "🍪🍪Una vez activado el cupón te preparo una tanda de galletas de chocolate para dártelas la próxima vez que nos veamos 🍪🍪",
        "rules": "Puedes activarlo tantas veces como quieras",
        "canjeable": True,
        "serio": True,
        "rules": "Puedes activarlo tantas veces como quieras",
        "toggle": True,
        "activado": False,
        "img": "static/img/gargamelGalletas.jpeg", 
        "date": "2025-02-03"
        },
}

# Lista para almacenar los cupones desbloqueados
unlocked_coupons = []

@app.route('/')
def index():
    today = datetime.now().strftime('%Y-%m-%d')

    # Leer la cookie correctamente 
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    try:
        unlocked_coupons_data = json.loads(unlocked_coupons_cookie)
    except json.JSONDecodeError:
        unlocked_coupons_data = {}

    # Verificar si el cupón de hoy ya está desbloqueado
    if today in unlocked_coupons_data:
        return redirect(url_for('coupon_list'))  # Evitar mostrar el regalo de nuevo

    if today in coupons:
        coupon = coupons[today]
        return render_template('index.html', today=today, coupon=coupon)
    else:
        return render_template('no_coupon.html')


from flask import jsonify

@app.route('/unlock/<date>')
def unlock_coupon(date):
    if date in coupons:
        coupon = coupons[date]

        # Leer y decodificar la cookie correctamente
        unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
        try:
            unlocked_coupons = json.loads(unlocked_coupons_cookie)
        except json.JSONDecodeError:
            unlocked_coupons = {}
        # Original date string
        date_str = coupon["date"]

        # Define the input format
        input_format = "%Y-%m-%d"

        # Define the output format
        output_format = "%d/%m/%Y"

        # Convert string to datetime object
        date_obj = datetime.strptime(date_str, input_format)

        # Convert back to string in the new format
        new_date_str = date_obj.strftime(output_format)

        # Si el cupón no está en la lista, agregarlo
        if date not in unlocked_coupons:
            unlocked_coupons[date] = {
                "code": coupon["code"],
                "description": coupon["description"],
                "img": coupon["img"],
                "mensaje_desbloqueo": coupon["mensaje_desbloqueo"],
                "titulo": coupon["titulo"],
                "date": new_date_str,
                "redeemed": False
            }

        # Guardar la cookie actualizada
        response = make_response(jsonify(coupon))
        response.set_cookie('unlocked_coupons', json.dumps(unlocked_coupons), httponly=True, max_age=60*60*24*365)
        return response
    else:
        return jsonify({"error": "Cupón no disponible."}), 404


@app.route('/redeem/<code>' , methods=['POST'])
def redeem_coupon(code):
    # Leer y decodificar la cookie
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    try:
        unlocked_coupons = json.loads(unlocked_coupons_cookie)
    except json.JSONDecodeError:
        unlocked_coupons = {}

    # Marcar el cupón como activado si existe
    for date, coupon in unlocked_coupons.items():
        if coupon["code"] == code:
            coupon["redeemed"] = True

    # Guardar la cookie actualizada
    response = make_response(jsonify({"message": "Cupón activado"}))
    response.set_cookie('unlocked_coupons', json.dumps(unlocked_coupons), httponly=True, max_age=60*60*24*365)
    return response
    

@app.route('/unlocked/<code>')
def unlocked_coupon(code):
# Buscar el cupón en los desbloqueados
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    unlocked_coupons = json.loads(unlocked_coupons_cookie)

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
    print(json.dumps(coupons_list, indent=4))
    print("Cupones desbloqueados:", coupons_list)  

    return render_template('coupon_list.html', coupons=coupons_list)

@app.route('/coupon/<code>')
def coupon_detail(code):
    # Leer y decodificar la cookie
    unlocked_coupons_cookie = request.cookies.get('unlocked_coupons', '{}')
    unlocked_coupons = json.loads(unlocked_coupons_cookie)
    
    # Buscar el cupón por su código
    coupon = next((coupon for coupon in unlocked_coupons.values() if coupon["code"] == code), None)
    if coupon:
        return render_template('coupon_detail.html', coupon=coupon)
    else:
        return "Cupón no encontrado."

if __name__ == '__main__':
    app.run(debug=True)