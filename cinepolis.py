from flask import Flask, request, render_template  

app = Flask(__name__)


class Cinepolis:

    def __init__(self, nombre):

        self.nombre = nombre

        self.compradores = 0

        self.boletos = 0

        self.metodo = ""

        self.totalPagar = 0



    def asignarCompra(self, compradores, boletos):

        self.compradores = compradores

        self.boletos = boletos




    def clasificacionDescuentos(self):

        precioBoleto = 12.00

        totalPagar = self.boletos * precioBoleto  

        if self.boletos > 5:

            totalPagar *= 0.85 

        elif self.boletos > 3:

            totalPagar *= 0.90  

        self.totalPagar = totalPagar  

        return totalPagar





    def descuentoTarjeta(self):

        self.totalPagar *= 0.90 






    def __str__(self):

        return f"{self.nombre}, {self.totalPagar:.2f}"





    @staticmethod
    def validarCantidadBoletos(compradores, boletos):

        limiteBoletoPersona = 7

        return boletos <= compradores * limiteBoletoPersona


@app.route('/Cinepolis', methods=["GET", "POST"])

def cinepolis():

    totalFinal = None  

    error = None



    if request.method == "POST":
        
        nombre = request.form["nombre"]

        cantidad_compradores = int(request.form["compradores"])

        boletos = int(request.form["boletos"])

        cineco = request.form["tarjeta"]

      

        if not Cinepolis.validarCantidadBoletos(cantidad_compradores, boletos):

            error = "No puedes comprar más de 7 boletos por persona."

            return render_template("Cinepolis.html", error=error, totalFinal=None, nombre=nombre, compradores=cantidad_compradores, boletas=boletos, cineco=cineco)

       
        cliente = Cinepolis(nombre)

        cliente.asignarCompra(cantidad_compradores, boletos)

        totalFinal = cliente.clasificacionDescuentos()  


        
        if cineco == "si":

            cliente.descuentoTarjeta()

            totalFinal = cliente.totalPagar  

            

    return render_template("Cinepolis.html", totalFinal=totalFinal, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
