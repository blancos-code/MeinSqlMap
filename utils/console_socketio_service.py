from flask_socketio import SocketIO


def display_to_console(sql_map_output: str, socketio: SocketIO, url: str, index: int):
    sql_map_state = 'none'
    if sql_map_output:
        sql_map_output = sql_map_output.strip()

        sql_map_state = 'loading'
        if 'ending' in sql_map_output and sql_map_state != 'success':
            sql_map_state = 'failure'
        if 'available databases' in sql_map_output:
            sql_map_state = 'success'

        socketio.emit('console_output',
                      {'url': url, 'data': sql_map_output, 'index': index, 'sql_map_state': sql_map_state})

    return sql_map_state