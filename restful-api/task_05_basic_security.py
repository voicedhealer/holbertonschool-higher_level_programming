from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required, get_jwt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user": 
        {"username": "user", "password": generate_password_hash("password"), "role": "user"},
    "admin":
        {"username": "admin", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):     
      if username in users and check_password_hash(users[username]["password"], password):
        return username
        return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    if username in users and check_password_hash(username["password"], password):
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

@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt()
    user_role = claims.get('role', 'user')
    
    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == '__main__':
    app.run(debug=True)
