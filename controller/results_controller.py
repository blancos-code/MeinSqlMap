from flask import Blueprint, render_template, session
from flask_socketio import SocketIO
from urllib.parse import urlparse

from utils import bdd_service as database
from utils.sqlmap_service import handle_start_scan

results_blueprint = Blueprint('results', __name__)

socketio = SocketIO()

def get_domain_name(url: str) -> str:
    parsed_uri = urlparse(url)
    domain_name = '{uri.netloc}'.format(uri=parsed_uri)
    return domain_name

@results_blueprint.route("/results")
def results():
    search_results = session.get('results', [])
    for index, result in enumerate(search_results):
        if result['is_valid_for_pentesting']:
            if (database.isInDatabase('site',result['url'])):
                return render_template("search.html")
            else:   
                database.insert_site(result['url'], get_domain_name(result['url']))
                handle_start_scan({'url': result['url'], 'index': index}, socketio)
    return render_template("results.html", results=search_results)
