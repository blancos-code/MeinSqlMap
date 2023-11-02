from flask import Blueprint, render_template, request, redirect, url_for, session
import requests

search_blueprint = Blueprint('search', __name__)

GOOGLE_SEARCH_API_ENDPOINT = "https://www.googleapis.com/customsearch/v1"
API_KEY = "AIzaSyBkyDVIntg2fkRT8d-ROxoeMa2GKEcv8gI"
CX = "509596f2cacfb4f10"


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
    for page in range(int(start), int(start) + int(page_count)):
        params = {
            "q": "inurl:" + query,
            "key": API_KEY,
            "cx": CX,
            "start": int(page)
        }
        if page > int(start) + int(page_count):
            print(page)
            print(int(start))
            print(int(page_count))
            break

        response = requests.get(GOOGLE_SEARCH_API_ENDPOINT, params=params)
        items = response.json().get("items", [])
        for item in items:
            result = {'url': item.get('link', '')}
            result['is_valid_for_pentesting'] = is_url_valid(result['url'])
            results.append(result)

    print(results)

    return results


def is_url_valid(url):
    query = session.get('query', '')

    return ('=' in url) or (("/" + query + "/") in url)
