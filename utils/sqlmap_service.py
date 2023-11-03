import shlex
import subprocess
import threading
from utils.console_socketio_service import display_to_console


def handle_start_scan(data, socketio):
    url = data['url']
    index = data['index']
    thread = threading.Thread(target=run_sqlmap, args=(url, index, socketio))
    thread.start()


def run_sqlmap(url, index, socketio):
    command = f"python sql_map/sqlmap.py -u {url} --batch -dbs"
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    while True:
        output = process.stdout.readline()
        if not output and process.poll() is not None:
            break

        sql_map_state = display_to_console(output, socketio, url, index)

    rc = process.poll()
    return rc
