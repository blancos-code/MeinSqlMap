from flask import Flask, Blueprint
import sqlite3

app = Flask(__name__)

create_connection_blueprint = Blueprint('test', __name__)


# CREATE TABLE IF NOT EXISTS site_proprietaire (
#             nom_de_domaine text FOREIGN KEY ,
#             proprietaire_id integer FOREIGN KEY
#         );

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS site (
            url text PRIMARY KEY,
            nom_de_domaine text NOT NULL,
            isVulnerable boolean
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proprietaire (
                id integer PRIMARY KEY,
                prenom text,
                nom text,
                mail text,
                telephone text
        );
    """)

def insert_site(conn,url,nom_de_domaine,isVulnerable):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO `site` (`url`, `nom_de_domaine`, `isVulnerable`) VALUES
                   """+ '("' + url + '", "' + nom_de_domaine + '",' + str(isVulnerable) + ');')
    


@create_connection_blueprint.route("/test", methods=["GET", "POST"])
def create_connection():
    conn = None
    response = ""
    try:
        conn = sqlite3.connect('data/bdd.db')
        print(sqlite3.version)
        if conn:
            create_table(conn)
            insert_site(conn,"www.google.com",'google.com',False)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM site")
            rows = cursor.fetchall()
            for row in rows:
                response += str(row) + '<br>'
            conn.close()
    except sqlite3.Error as e:
        print(e)
        
    return response if response else "No data"


app.register_blueprint(create_connection_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
