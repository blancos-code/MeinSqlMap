from flask import Blueprint, render_template, session
from flask_socketio import SocketIO

from utils import bdd_service as database
from utils.sqlmap_service import handle_start_scan

results_blueprint = Blueprint('results', __name__)

socketio = SocketIO()


@results_blueprint.route("/results")
def results():
    search_results = session.get('results', [])
    for index, result in enumerate(search_results):
        if result['is_valid_for_pentesting']:
            database.insert_site(result['url'], 'Tkt nom de domaine')

            handle_start_scan({'url': result['url'], 'index': index}, socketio)
    return render_template("results.html", results=search_results)
