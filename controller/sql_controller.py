from flask import Blueprint, jsonify, render_template, request, redirect, url_for, session
import sqlite3
from flask_socketio import SocketIO
from urllib.parse import urlparse

from utils import bdd_service as database
from utils.sqlmap_service import handle_start_scan

sql_blueprint = Blueprint('sql_blueprint', __name__)

def getData():
    conn = sqlite3.connect('data/bdd.db')  # Changez ceci pour le chemin de votre base de données
    cursor = conn.cursor()
    # Récupère le nom de toutes les tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    data = {}  # Dictionnaire pour stocker les données de toutes les tables
    for table in tables:
        table = table[0]
        cursor.execute(f"SELECT * FROM {table}")
        data[table] = cursor.fetchall()
    conn.close()
    
    return data


@sql_blueprint.route("/sql", methods=["GET", "POST"])
@sql_blueprint.route("/sql/<int:page>", methods=["GET", "POST"])
def display(page=1):
    data = getData()
    items_per_page = 6
    page_start_historique = (page - 1) * items_per_page
    page_end_historique = page_start_historique + items_per_page
    historique_data = data['historique'][page_start_historique:page_end_historique]

    return render_template("sql.html", database_data=data, site=data['site'], historique=historique_data)

@sql_blueprint.route("/sql/history/delete/<int:id_history>", methods=["GET", "POST"])
def delete_history(id_history):
    database.delete(id_history)

    return redirect(url_for('database_blueprint.display'))


def get_domain_name(url: str) -> str:
    parsed_uri = urlparse(url)
    domain_name = '{uri.netloc}'.format(uri=parsed_uri)
    return domain_name


@sql_blueprint.route('/sql_add_site', methods=['POST'])
def insert_site():
    # Récupérez les données soumises par le formulaire
    data = request.get_json()
    user_input = data['user_input']

    # Effectuez les opérations souhaitées avec les données
    database.insert_site(user_input, get_domain_name(user_input))

    response = {
        'result': "Opérations effectuées avec succès"
    }
    return jsonify(response)


@sql_blueprint.route('/sql_add_historique', methods=['POST'])
def insert_historique():
    # Récupérez les données soumises par le formulaire
    data = request.get_json()
    recherche = data['inputTextHistorique']
    pageDepart = data['inputNumberHistorique']
    nbRequete = data['inputNumberRequete']

    # Effectuez les opérations souhaitées avec les données
    database.insert_historique(recherche,pageDepart,nbRequete)

    response = {
        'result': "Opérations effectuées avec succès"
    }
    return jsonify(response)


