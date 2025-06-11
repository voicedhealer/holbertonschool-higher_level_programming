#!/usr/bin/python3
'''
Ce module fournit un ensemble de routes
et de méthodes pour sécuriser l'accès HTTP
dans le contexte d'un serveur Flask simple.
'''

# Import des modules nécessaires de Flask
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

# Initialisation de l'application Flask
app = Flask(__name__)

# Dictionnaire des utilisateurs comme demander dans l'énoncé
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Initialisation de l'authentification Basic
auth = HTTPBasicAuth()

# Fonction de vérification pour Basic Auth
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    # Vérifie que l'utilisateur existe et que le mot de passe est correct
    if user and check_password_hash(user["password"], password):
        return user  # Retourne l'objet utilisateur si authentifié
    return None     # Sinon, retourne None échec d'auth

# Configuration de la clé secrète JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Route protégée par Basic Auth
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Route pour obtenir un token JWT après login (POST)
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401  # Erreur si mauvais identifiants

# Route protégée par JWT
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Route protégée par JWT réservée aux admins
@app.route('/admin-only')
@jwt_required()
def admin_only():
    identity = get_jwt_identity()  # Récupère l'identité du token JWT
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403  # Refus si pas admin
    return "Admin Access: Granted"

# Gestionnaire d'erreur : token manquant ou invalide
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

# Gestionnaire d'erreur : token JWT mal formé
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

# Gestionnaire d'erreur : token JWT expiré
@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

# Point d'entrée principal du serveur Flask
if __name__ == "__main__":
    app.run(debug=True)
