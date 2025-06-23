# task_02_requests.py

import requests
import csv
from typing import List, Dict, Any

# L'URL de l'API que nous allons interroger.
API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """
    Récupère les posts depuis l'API JSONPlaceholder et affiche leurs titres.

    Cette fonction envoie une requête GET à l'API. Si la requête réussit
    (code 200), elle affiche le code de statut, puis parcourt la liste
    des posts et affiche le titre de chacun.
    """
    print("Fetching posts to print...")
    try:
        response = requests.get(API_URL)
        
        # Affiche le code de statut de la réponse HTTP.
        print(f"Status Code: {response.status_code}")

        # Vérifie si la requête a réussi.
        if response.status_code == 200:
            # Convertit la réponse JSON en une liste de dictionnaires Python.
            posts: List[Dict[str, Any]] = response.json()
            
            # Itère sur chaque post et affiche son titre.
            for post in posts:
                print(post['title'])
                
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def fetch_and_save_posts():
    """
    Récupère les posts depuis l'API et les sauvegarde dans un fichier CSV.

    Si la requête est fructueuse, cette fonction structure les données
    en une liste de dictionnaires (avec les clés 'id', 'title', 'body')
    et les écrit dans un fichier nommé 'posts.csv'.
    """
    print("\nFetching posts to save...")
    try:
        response = requests.get(API_URL)
        
        # Vérifie si la requête a réussi avant de tenter de sauvegarder.
        if response.status_code == 200:
            posts: List[Dict[str, Any]] = response.json()
            
            # Prépare les données pour le CSV, en ne gardant que les champs requis.
            data_to_save = []
            for post in posts:
                data_to_save.append({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })

            # Définit les noms des colonnes pour le fichier CSV.
            fieldnames = ['id', 'title', 'body']
            
            # Ouvre le fichier en mode écriture.
            # newline='' évite les lignes vides indésirables entre les enregistrements.
            # encoding='utf-8' assure la compatibilité avec les caractères spéciaux.
            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                # Crée un DictWriter, qui mappe les dictionnaires aux lignes du CSV.
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                # Écrit la ligne d'en-tête (id, title, body).
                writer.writeheader()
                
                # Écrit toutes les lignes de données en une seule fois.
                writer.writerows(data_to_save)
            
            print("Data saved to posts.csv")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
