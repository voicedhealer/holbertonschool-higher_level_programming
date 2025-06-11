from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Utilise une clé plus forte en production
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Structure de données avec rôles comme demandé dans l'exercice
users = {
    "user1": {
        "username": "user1", 
        "password": generate_password_hash("password"), 
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"), 
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

# Gestion des erreurs d'authentification Basic Auth
@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized"}), 401

# Gestion des erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# Routes Basic Authentication
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Routes JWT Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    username = data['username']
    password = data['password']
    
    # Vérifier les identifiants
    if username in users and check_password_hash(users[username]["password"], password):
        # Inclure les informations utilisateur dans le token
        additional_claims = {"role": users[username]["role"]}
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Route avec contrôle d'accès basé sur les rôles
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    # Récupérer le rôle depuis le token JWT
    from flask_jwt_extended import get_jwt
    claims = get_jwt()
    user_role = claims.get('role', 'user')
    
    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token)

if __name__ == '__main__':
    app.run(debug=True)
