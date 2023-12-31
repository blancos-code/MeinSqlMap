from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3


database_blueprint = Blueprint('database_blueprint', __name__)


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


@database_blueprint.route("/database", methods=["GET", "POST"])
@database_blueprint.route("/database/<int:page>", methods=["GET", "POST"])
def display(page=1):
    data = getData()
    items_per_page = 6
    page_start_historique = (page - 1) * items_per_page
    page_end_historique = page_start_historique + items_per_page
    historique_data = data['historique'][page_start_historique:page_end_historique]

    return render_template("database.html", database_data=data, site=data['site'], historique=historique_data)
