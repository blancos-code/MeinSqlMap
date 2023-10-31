from flask import Flask, render_template, request
import requests

app = Flask(__name__)

GOOGLE_SEARCH_API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
API_KEY = "AIzaSyCvl-lGhRJ12dYAnhAr1HgKdWmINWABus8"
CX = "57447145afad04e1b"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            params = {
                "q": query,
                "key": API_KEY,
                "cx": CX,
                "start": 21
            }
            response = requests.get(GOOGLE_SEARCH_API_ENDPOINT, params=params)
            results = response.json().get("items", [])
            return render_template("results.html", results=results)
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)
