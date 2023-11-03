from flask import Flask, render_template, session
from flask_socketio import SocketIO
from controller.search_controller import search_blueprint
import threading
import subprocess
import shlex

app = Flask(__name__)

app.secret_key = 'super_secret'
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

app.register_blueprint(search_blueprint)


@app.route("/")
def home():
    return render_template("home.html")


@socketio.on('start_scan')
def handle_start_scan(data):
    url = data['url']
    index = data['index']
    thread = threading.Thread(target=run_sqlmap, args=(url, index))
    thread.start()


@app.route("/results")
def results():
    search_results = session.get('results', [])
    for index, result in enumerate(search_results):
        if result['is_valid_for_pentesting']:
            handle_start_scan({'url': result['url'], 'index': index})
    return render_template("results.html", results=search_results)


def run_sqlmap(url, index):
    command = f"python sql_map/sqlmap.py -u {url} --batch -dbs"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    socketio.emit('console_output', {'data': url + "\n", 'index': index})

    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break
        if output:
            if output:
                output = output.strip()
                if 'CRITICAL' in output:
                    sql_map_state = 'failure'
                elif 'available databases' in output:
                    sql_map_state = 'success'
                else:
                    sql_map_state = 'loading'

                socketio.emit('console_output',
                              {'url': url, 'data': output, 'index': index, 'sql_map_state': sql_map_state})

            socketio.emit('console_output', {'url': url,'data': output.strip(), 'index': index, 'sql_map_state': sql_map_state})
    rc = process.poll()
    return rc


if __name__ == "__main__":
    app.run(debug=True)
