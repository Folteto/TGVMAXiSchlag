#This program runs a wbeserver to managed the request to main.py and helps with the parameters
#@author ybeattie
#@version 1

from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
from threading import Timer

app = Flask(__name__)

def get_gares():
    '''Défini la liste de gare pour l'utilisateur puisse sélectionner'''
    with open('data/gares.txt', 'r') as file:
        gares = [line.strip() for line in file]
    return gares

@app.route('/')
def index():
    '''Définit la page d'accueil et de recherche'''
    gares = get_gares()
    return render_template('index.html', gares=gares)

@app.route('/search_gares', methods=['GET'])
def search_gares():
    return jsonify({'gares': get_gares()})

@app.route('/search', methods=['POST'])
def search():
    '''Fonciton de recherche et redirection vers l'output'''
    gare_depart = request.form['gare_depart']
    gare_arrivee = request.form['gare_arrivee']
    date_depart = request.form['date_depart']
    nombre_etapes = request.form.get('nombre_etapes', '')

    command = [
        'python3', 'main.py',
        '-d', gare_depart,
        '-a', gare_arrivee,
        '-t', date_depart
    ]
    if nombre_etapes:
        command.extend(['-s', nombre_etapes])

    # Exécuter la commande et capturer la sortie
    result = subprocess.run(command, capture_output=True, text=True)

    # Afficher le résultat sur la page web
    return render_template('result.html', result=result.stdout)

if __name__ == '__main__':
    print("Please clik here : http://127.0.0.1:5000")
    app.run()
    
    

