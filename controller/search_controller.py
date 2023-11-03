from flask import Blueprint, render_template, request, redirect, url_for, session
import requests
from utils import bdd_service as database

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
            websites_infos = []
            websites_infos = get_websites_infos_from_google(page_count, query, websites_infos, start)

            session['results'] = websites_infos
            session['query'] = query

            database.insert_historique(query,start,page_count)
            
            return redirect(url_for('results.results'))
    return render_template("search.html")


def get_websites_infos_from_google(page_count, query, websites_infos, start):
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
        websites = response.json().get("items", [])
        for website in websites:
            website_infos = {'url': website.get('link', '')}

            website_infos = update_websites_infos(website_infos)
            websites_infos.append(website_infos)

    return websites_infos


def is_url_valid_for_pentesting(url, query):
    return ('=' in url) or (("/" + query + "/") in url)


def update_websites_infos(website_infos):
    query = session.get('query', '')

    website_infos['is_valid_for_pentesting'] = is_url_valid_for_pentesting(website_infos['url'], query)
    website_infos['url'] = couper_url(website_infos['url'], query)

    return website_infos


def couper_url(url, query):
    index = url.find("/" + query + "/")
    if index == -1:
        return url

    nouvelle_url = url[:index + len(query) + 2] + '*'

    return nouvelle_url
