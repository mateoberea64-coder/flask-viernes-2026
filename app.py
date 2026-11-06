from flask import Flask, render_template

app = Flask(__name__)

@app.route("/SR.com")
def inicio():
    return render_template("index.html")

@app .route("/saludo/<nombre>")
def saludo(nombre):
    return "¡Quiero rretruco!"

if __name__ == "__main__":
    app.run(debug=True)

