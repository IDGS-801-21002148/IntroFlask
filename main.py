from flask import Flask,render_template

app=Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hola")
def hola():
    return "<h1>Hola, Mundo!</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>Hola, {user}!</h1>"

@app.route("/numero/<int:numero>")
def number(numero):
    return f"<h1>El numero es {numero}!</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
 <form action="">
        <label for="">Name</label>
        <input type="text" id="name" name="name" required>

        <label for="">APaterno</label>
        <input type="text" id="APaterno" name="APaterno" required>
    </form>
           '''

if _name== "main_":
    app.run(debug=True, port=3000)