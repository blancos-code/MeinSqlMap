from flask import Flask, render_template

from controller.search_controller import search_blueprint
from controller.results_controller import results_blueprint, socketio
from controller.bdd_controller import database_blueprint
from controller.sql_controller import sql_blueprint
from utils.bdd_service import create_database_tables


app = Flask(__name__)

app.secret_key = 'super_secret'
app.config['SECRET_KEY'] = 'secret!'

app.register_blueprint(search_blueprint)
app.register_blueprint(results_blueprint)
app.register_blueprint(database_blueprint)
app.register_blueprint(sql_blueprint)

socketio.init_app(app)
create_database_tables()

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
