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
        page_count = request.form.get("page_count")

        if query:
            results = []

            results = get_results_from_google(page_count, query, results, start)

            session['results'] = results
            session['query'] = query
            return redirect(url_for('results'))
    return render_template("search.html")


def get_results_from_google(page_count, query, results, start):

    for page in range(int(start), int(start + page_count)):
        params = {
            "q": "inurl:" + query,
            "key": API_KEY,
            "cx": CX,
            "start": page
        }

        response = requests.get(GOOGLE_SEARCH_API_ENDPOINT, params=params)
        items = response.json().get("items", [])
        print(response.json())
        for item in items:
            result = {'url': item.get('link', '')}
            result['is_valid_for_pentesting'] = is_url_valid(result['url'])
            results.append(result)

    return results

def is_url_valid(url):
    query = session.get('query', '')

    return ('=' in url) or (("/" + query + "/") in url)
