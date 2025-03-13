from flask import Flask, render_template, request, jsonify, url_for, g, flash
from datetime import datetime
from flask_wtf.csrf import CSRFProtect
import forms
import forms2

app = Flask(__name__)
app.secret_key = "secret key"
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request():
    g.user = "PEPE"
    print("before1")

@app.after_request
def after_request(response):
    print("after3")
    return response

class Zodiaco:
    def configurar_rutas(self, app):
        @app.route("/zodiaco", methods=["GET", "POST"])
        def zodiaco_index():
            usuario = None
            form = forms2.UserForm(request.form)
            if request.method == "POST" and form.validate():
                nombre = form.nombre.data
                apellido_p = form.apellido_p.data
                apellido_m = form.apellido_m.data
                dia = int(form.dia.data)
                mes = int(form.mes.data)
                anio = int(form.anio.data)
                sexo = form.sexo.data

                usuario = self.datos(nombre, apellido_p, apellido_m, dia, mes, anio, sexo)

                mensaje = f"Datos de {nombre} guardados correctamente."
                flash(mensaje)

            return render_template("ZodiacoChino.html", form=form, usuario=usuario)

    def datos(self, nombre, apellido_p, apellido_m, dia, mes, anio, sexo):
        edad = self.edadUsuario(anio)
        signo_chino, imagen_signo = self.signo(anio)
        return {
            "nombre": nombre,
            "apellido_p": apellido_p,
            "apellido_m": apellido_m,
            "fecha_nacimiento": f"{dia}/{mes}/{anio}",
            "edad": edad,
            "sexo": sexo,
            "signo_chino": signo_chino,
            "imagen_signo": imagen_signo
        }

    def signo(self, anio):
        signos = ["mono", "gallo", "perro", "cerdo", "raton", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "cabra"]
        signo = signos[anio % 12]
        imagen = f"static/img/{signo.lower()}.jpg"
        return signo, imagen

    def edadUsuario(self, anio_nacimiento):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - anio_nacimiento
        return edad

@app.route('/')
def index():
    titulo = "IDGS801"
    lista = ["Juan", "Pedro", "Maria", "Jose"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/HOLA')
def hola():
    return "<h1>Hola, Mundo!-- HOLA --</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>HOLA: {user}</h1>"

@app.route("/numero/<int:n1>")
def numero(n1):
    return f"<h1>Numero: {n1}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>HOLA: {username} - TU ID ES: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Juan"):
    return f"<h1>Hola: {param}</h1>"

@app.route("/operas")
def operas():
    return '''
    <form action="/procesar" method="post">
        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        <label for="email">Correo:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <button type="submit">Enviar</button>
    </form>
    '''

@app.route("/procesar", methods=["POST"])
def procesar():
    return "<h1>Formulario enviado correctamente</h1>"

@app.route("/resultado", methods=["POST"])
def result():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    operacion = request.form.get("operacion")

    try:
        n1 = float(n1)
        n2 = float(n2)

        if operacion == "suma":
            resultado = "{} + {} = {}".format(n1, n2, n1 + n2)
        elif operacion == "resta":
            resultado = "{} - {} = {}".format(n1, n2, n1 - n2)
        elif operacion == "division":
            resultado = "Error: No se puede dividir por cero" if n2 == 0 else "{} / {} = {}".format(n1, n2, n1 / n2)
        else:
            resultado = "La multiplicación de {} x {} es {}".format(n1, n2, n1 * n2)

    except ValueError:
        resultado = "Datos inválidos"

    return render_template("OperasBas.html", resultado=resultado, n1=n1, n2=n2, operacion=operacion)

@app.route("/Alumnos", methods=["GET", "POST"])
def Alumnos():
    mat = ''
    nom = ''
    ape = ''
    email = ''
    
    alumno_clas = forms.UserForm(request.form)
    if request.method == "POST" and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data

        mensaje = 'BIENVENIDO {}'.format(nom)
        flash(mensaje)

    return render_template("Alumnos.html", form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)

zodiaco = Zodiaco()
zodiaco.configurar_rutas(app)

if __name__ == "__main__":
    csrf.init_app(app)
    
    app.run(debug=True, port=5000)
