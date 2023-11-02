from flask import Blueprint, render_template, request, redirect, url_for, session
import requests

search_blueprint = Blueprint('search', __name__)

GOOGLE_SEARCH_API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
API_KEY = "AIzaSyCvl-lGhRJ12dYAnhAr1HgKdWmINWABus8"
CX = "57447145afad04e1b"


@search_blueprint.route("/search", methods=["GET", "POST"])
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
                result['isValidForPentesting'] = is_url_valid(result['url'])
                results.append(result)

            session['results'] = results
            session['query'] = query
            return redirect(url_for('results'))
    return render_template("search.html")


def is_url_valid(url):
    query = session.get('query', '')

    return ('=' in url) or (("/" + query + "/") in url)
