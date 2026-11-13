from flask import Flask, render_template, request, redirect

app = Flask(__name__)

respuestas = []
@app.route("/")
def inicio():
    return render_template("index.html")
@app.route("/formulario", methods= ["GET", "POST"])
def mandar_formulario():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        mensaje = request.form.get("mensaje", "").strip()
        if not nombre or not mensaje:
            return "Completa todos los datos", 400
        nueva_respuesta = {
            "nombre":nombre,
            "mensaje":mensaje
        }
        respuestas.append(nueva_respuesta)
        return redirect("/")
    return render_template("Formulario.html")

@app.route("/respuestas")
def ver_respuestas(): 
    return render_template("respuestas.html", mensajes = respuestas)

@app .route("/saludo/<nombre>")
def saludo(nombre):
    return "¡Quiero rretruco!"

if __name__ == "__main__":
    app.run(debug=True)

