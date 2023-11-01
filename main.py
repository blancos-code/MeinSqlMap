import threading

from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO
import requests
import subprocess
import shlex

app = Flask(__name__)

GOOGLE_SEARCH_API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
API_KEY = "AIzaSyCvl-lGhRJ12dYAnhAr1HgKdWmINWABus8"
CX = "57447145afad04e1b"
app.secret_key = 'super_secret'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        start = request.form.get("start")
        if query:
            params = {
                "q": "inurl:" + query,
                "key": API_KEY,
                "cx": CX,
                "start": start
            }
            response = requests.get(GOOGLE_SEARCH_API_ENDPOINT, params=params)
            items = response.json().get("items", [])

            results = []
            for item in items:
                result = {'url': item.get('link', '')}
                result['isValidForPentesting'] = isUrlValid(result['url'])
                results.append(result)

            session['results'] = results
            session['query'] = query
            return redirect(url_for('results'))
    return render_template("search.html")


@app.route("/results")
def results():
    results = session.get('results', [])
    for index, result in enumerate(results):
        if result['isValidForPentesting']:
            handle_start_scan({'url': result['url'], 'index': index})
    return render_template("results.html", results=results)


def isUrlValid(url):
    query = session.get('query', '')

    return ('=' in url) or ("/" + query + "/" in url)


@socketio.on('start_scan')
def handle_start_scan(data):
    url = data['url']
    index = data['index']
    thread = threading.Thread(target=run_sqlmap, args=(url, index))
    thread.start()


def run_sqlmap(url, index):
    command = f"python sql_map/sqlmap.py -u {url} --batch -dbs"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break
        if output:
            print(output.strip())
            socketio.emit('console_output', {'data': output.strip(), 'index': index})
    rc = process.poll()
    return rc



if __name__ == "__main__":
    app.run(debug=True)
