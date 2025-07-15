# README : Python Server Side Rendering

Bienvenue dans ce projet dédié au **Server Side Rendering (SSR) avec Python** !  
Ce guide vous accompagnera pour comprendre, configurer et exploiter le rendu côté serveur afin de générer des pages web dynamiques.

## Objectifs du Projet

- Découvrir le principe du SSR (génération HTML dynamique côté serveur)
- S’initier à la création de templates avec un moteur comme Jinja2
- Manipuler des routes HTTP pour générer du HTML côté serveur
- Comprendre la différence avec le rendu côté client (AJAX, JavaScript)
- Concevoir des sites dynamiques et interactifs _sans recourir uniquement au JavaScript_

## Prérequis

- Connaissances de base en Python
- Bases sur les frameworks web (ex : Flask, Django) recommandées mais non indispensables
- Notions HTML demandées

## Contenus et Étapes clés

### 1. Qu’est-ce que le Server Side Rendering ?

Le SSR est une technique où le **HTML est généré sur le serveur** (via du code Python par exemple), puis envoyé tout prêt au navigateur du client :  
- Avantages : SEO amélioré, chargement initial rapide, support d’anciens navigateurs
- Utilisé notamment dans Flask, Django, Ruby on Rails, PHP, etc.

### 2. Installation et Structure du projet

```
.
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```
- **templates/** : contient les fichiers HTML (templates Jinja)
- **app.py** : code principal du serveur
- **requirements.txt** : dépendances Python à installer

### 3. Exemples de rendu côté serveur

- Utilisation de **Flask** :
    ```python
    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', name="Holberton")
    ```

- Template Jinja :
    ```html
    
    
    
      Bienvenue {{ name }} !
    
    
    ```

### 4. Lancer l’application

1. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```
2. Lancez le serveur :
    ```sh
    python app.py
    ```
3. Ouvrez votre navigateur sur `http://localhost:5000`

## Fonctionnalités typiques à mettre en place

- Affichage de variables dynamiques dans le template HTML
- Passage de listes/tableaux Python pour générer des listes HTML dynamiques
- Gestion de plusieurs routes : `/`, `/about`, `/articles/`, etc.
- Utilisation des blocs `if`, `for` de Jinja2 dans les templates
- Optionnel : gestion de formulaires, messages flash…

## Bonnes pratiques

- Séparez le code Python de vos templates HTML
- Nommer vos routes et templates de façon explicite
- N’affichez jamais de données non “nettoyées” (risque XSS)
- Privilégiez `render_template()` pour toute page générée

## Liens utiles

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Jinja2 Templating](https://jinja.palletsprojects.com/)
- [Introduction au SSR](https://developer.mozilla.org/fr/docs/Glossary/Server-side_rendering)
- [Tutoriel Flask débutant](https://pythonbasics.org/flask-tutorial/)

## Auteurs

- Projet réalisé dans le cadre de **Holberton School**
- Rédigé par : Vivien Bernardot