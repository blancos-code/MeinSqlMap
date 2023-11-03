import time

from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from datetime import date
import sqlite3

def create_database_tables():
    conn = sqlite3.connect('data/bdd.db')
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS site_proprietaire (
            nom_de_domaine text,
            proprietaire_id integer,
            PRIMARY KEY (nom_de_domaine, proprietaire_id),
            FOREIGN KEY (nom_de_domaine) REFERENCES site (nom_de_domaine),
            FOREIGN KEY (proprietaire_id) REFERENCES proprietaire (id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historique (
            id integer PRIMARY KEY AUTOINCREMENT,
            recherche text,
            page_depart integer NOT NULL,
            nb_requete integer NOT NULL,
            date_recherche DATE DEFAULT (date('now')),
            temps TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)


def insert_site(url, nom_de_domaine):
    conn = sqlite3.connect('data/bdd.db')
    cursor = conn.cursor()
    for _ in range(100):
        try:
            cursor.execute("""
                INSERT INTO `site` (`url`, `nom_de_domaine`, `isVulnerable`) VALUES
                           """ + '("' + url + '", "' + nom_de_domaine + '",' + '0' + ');')
            conn.commit()
            break
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("La base de données est verrouillée, nouvelle tentative...")
                time.sleep(1)  # Attendre un peu avant de réessayer
            else:
                raise e
        finally:
            cursor.close()




def insert_historique(recherche,page_depart,nb_requete):
    conn = sqlite3.connect('data/bdd.db')
    cursor = conn.cursor()

    for _ in range(100):
        try:
            cursor.execute("""
                INSERT INTO `historique` (`recherche`, `page_depart`, `nb_requete`) VALUES
                        """ + '("' + recherche + '",' + page_depart + ',' + nb_requete + ');'
                           )
            conn.commit()
            break
        except sqlite3.OperationalError as e:
            if "locked" in str(e):
                print("La base de données est verrouillée, nouvelle tentative...")
                time.sleep(1)  # Attendre un peu avant de réessayer
            else:
                raise e
        finally:
            cursor.close()



