import threading
import subprocess
import shlex

from utils.console_socketio_service import display_to_console
from flask import Blueprint, render_template, session
from flask_socketio import SocketIO

results_blueprint = Blueprint('results', __name__)

socketio = SocketIO()


@results_blueprint.route("/results")
def results():
    search_results = session.get('results', [])
    for index, result in enumerate(search_results):
        if result['is_valid_for_pentesting']:
            handle_start_scan({'url': result['url'], 'index': index})
    return render_template("results.html", results=search_results)


def handle_start_scan(data):
    url = data['url']
    index = data['index']
    thread = threading.Thread(target=run_sqlmap, args=(url, index))
    thread.start()


def run_sqlmap(url, index):
    command = f"py sql_map/sqlmap.py -u {url} --batch -dbs"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    socketio.emit('console_output', {'data': url + "\n", 'index': index})

    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break

        display_to_console(output, socketio, url, index)

    rc = process.poll()
    return rc
