#This program runs a wbeserver to managed the request to main.py and helps with the parameters
#@author ybeattie
#@version 1

from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
from threading import Timer
from main import main

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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

@app.route('/more')
def about_us():
    '''Définit la page "About us""'''
    return render_template('info.html')

@app.route('/search_gares', methods=['GET'])
def search_gares():
    '''Permet d'aider l'utilisateur avec la liste des gares qui matchent'''
    return jsonify({'gares': get_gares()})


@app.route('/search', methods=['POST'])
def search():
    '''Fonction de recherche et redirection vers l'output'''
    gare_depart = request.form['gare_depart']
    gare_arrivee = request.form['gare_arrivee']
    date_depart = request.form['date_depart']
    nombre_etapes = request.form.get('nombre_etapes', '')

    args = Namespace(depart=gare_depart, arrivee=gare_arrivee, date=date_depart, steps=nombre_etapes, hour="00:01", force=False, list_gares=False, propale=False)
    
    direct_trains, indirect_trains = main(args)

    # Afficher le résultat sur la page web
    return render_template('result.html', resultats=[direct_trains, indirect_trains])

if __name__ == '__main__':
    print("Please clik here : http://127.0.0.1:5000")
    app.run(debug=True)
    
    

