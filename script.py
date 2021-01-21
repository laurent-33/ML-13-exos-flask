from flask import Flask, render_template, request
app = Flask(__name__)

import logging
import mysql.connector
import os
import cgi

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

    pseudo_exist=False
    
    # insertion d'un utilisateur dans la base de données
    cnx = mysql.connector.connect(
        host='database', database='flask',
        user='user', password='exo'
    )
    cursor = cnx.cursor()

    query = ("INSERT INTO `utilisateurs` (nom, prenom, sexe, pseudo) VALUES (%s, %s, %s, %s)")
    
    try:
        cursor.execute(query, (nom, prenom, sexe, pseudo))
    except mysql.connector.errors.IntegrityError:
        logging.warning('ce pseudo est déjà utilisé')
    
    cursor.close()
    cnx.commit()

    cursor = cnx.cursor()    
    query = ("SELECT nom, prenom, sexe, pseudo FROM `utilisateurs`")
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    
    cnx.close()
    logging.warning(results)

    users_table = ''
    for user in results:
        users_table += '<tr>'
        for column in user:
            users_table += '<td>' + column + '</td>'
        users_table += '</tr>'

    logging.warning(users_table)

    return render_template(
        "bienvenue2.html",
        nom=nom,
        prenom=prenom,
        sexe=sexe,
        pseudo=pseudo,
        users_table=users_table
        )

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')
