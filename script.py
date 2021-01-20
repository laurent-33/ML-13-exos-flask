from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(
        "home.html",
        message = "hope you like this long rainbow sentence"
        )

@app.route("/next")
def suite():
    return render_template("page_suivante.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['username']
    processed_text = text.upper()
    return render_template("bienvenue.html", message=processed_text)

@app.route('/test-formulaire')
def formulaire_complet():
    return render_template("formulaire_full.html")

@app.route('/test-formulaire', methods=['POST'])
def formulaire_sent():
    nom = request.form['nom']
    prenom = request.form['prenom']
    sexe = request.form['sexe']
    pseudo = request.form['pseudo']
    return render_template(
        "bienvenue2.html",
        nom=nom,
        prenom=prenom,
        sexe=sexe,
        pseudo=pseudo
        )



if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')

