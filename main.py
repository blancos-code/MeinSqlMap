from flask import Flask, render_template

from controller.bdd_controller import create_connection_blueprint
from controller.search_controller import search_blueprint
from controller.results_controller import results_blueprint, socketio


app = Flask(__name__)

app.secret_key = 'super_secret'
app.config['SECRET_KEY'] = 'secret!'

app.register_blueprint(search_blueprint)
app.register_blueprint(create_connection_blueprint)
app.register_blueprint(results_blueprint)

socketio.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
