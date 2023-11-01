# MeinSqlMap

Automatisation de SqlMap avec une api google limitée à 100 requêtes (1000 sites) par jour en version gratuite.

## Configuration de l'API Google Custom Search

Cette application utilise l'API Google Custom Search pour effectuer des recherches sur internet et récupérer les résultats. Voici les étapes pour configurer et utiliser cette API dans votre projet :

### 1. Créer un projet sur Google Cloud Platform

1. Allez sur [Google Cloud Console](https://console.cloud.google.com/).
2. Cliquez sur le bouton "Select a project" en haut de la page.
3. Dans la fenêtre qui s'ouvre, cliquez sur "New Project".
4. Donnez un nom à votre projet, configurez l'emplacement si nécessaire, puis cliquez sur "Create".

### 2. Activer l'API Custom Search JSON API

1. Dans le tableau de bord de votre projet Google Cloud, utilisez la barre de recherche en haut et recherchez "Custom Search JSON API".
2. Sélectionnez "Custom Search JSON API" dans les résultats de recherche.
3. Cliquez sur le bouton "Enable" pour activer l'API pour votre projet.

### 3. Créer une Clé API

1. Dans le menu latéral, cliquez sur "Credentials".
2. Cliquez sur "Create Credentials" et sélectionnez "API key".
3. Une clé API sera générée pour vous. Copiez cette clé et conservez-la en lieu sûr, car vous en aurez besoin pour configurer votre application.

### 4. Configurer la Recherche Customisée

1. Allez sur [Google Custom Search](https://cse.google.com/cse/).
2. Cliquez sur "Add" pour créer un nouveau moteur de recherche.
3. Entrez les sites web que vous souhaitez inclure dans les recherches, configurez les autres paramètres selon vos besoins, puis cliquez sur "Create".
4. Une fois le moteur de recherche créé, copiez l'identifiant "CX" (Identifiant de moteur de recherche) qui vous sera affiché.

### 5. Configurer Votre Application

Dans main.py, remplacez la clé API et l'identifiant CX par ceux que vous avez obtenus lors des étapes précédentes.

```python
API_KEY = "votre_clé_api"
CX = "votre_identifiant_cx"
```

## Installation

Pour exécuter ce projet, vous aurez besoin de Python et de quelques bibliothèques. Suivez ces étapes pour installer les dépendances et exécuter le projet.

### Prérequis

- Python 3.7 ou version ultérieure
- pip (gestionnaire de paquets pour Python)

### Installation des dépendances

Clonez le dépôt Git et installez les paquets nécessaires à partir de `requirements.txt` :

```bash
git clone [https://your-repository-url.git](https://github.com/blancos-code/MeinSqlMap.git)
cd MeinSqlMap
pip install -r requirements.txt
```

### Exécution de l'application

Pour exécuter l'application, utilisez la commande suivante :

```bash
python main.py
```

## Usage

Après avoir démarré l'application, ouvrez votre navigateur et accédez à `http://127.0.0.1:5000/` pour interagir avec l'interface utilisateur.

## Contribuer

Les contributions sont toujours les bienvenues ! Voici comment vous pouvez les faire :

1. Fork the Repository
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
