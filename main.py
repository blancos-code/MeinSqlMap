from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)

GOOGLE_SEARCH_API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
API_KEY = "AIzaSyCvl-lGhRJ12dYAnhAr1HgKdWmINWABus8"
CX = "57447145afad04e1b"
app.secret_key = 'super_secret'


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
    # Récupérer les résultats de la session
    results = session.get('results', [])
    return render_template("results.html", results=results)


def isUrlValid(url):
    query = session.get('query', '')

    return ('=' in url) or ("/"+query+"/" in url)



if __name__ == "__main__":
    app.run(debug=True)
