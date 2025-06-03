from flask import Flask, request, jsonify
import os, psycopg2
from fonctions import verify_jwt

app = Flask(__name__)

USER_2FA = os.environ.get('USER_2FA')
PASSWORD_2FA = os.environ.get('PASSWORD_2FA')
DB_2FA = os.environ.get('DB_2FA')

DATABASE_URL = f"postgresql://{USER_2FA}:{PASSWORD_2FA}@db:5432/{DB_2FA}"

@app.route('/api', methods=['GET', 'POST'])
def api():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Token manquant"}), 401
    
    data = verify_jwt(token)
    if not data:
        return jsonify({"error": "Token invalide ou expire"}), 401
    
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            if request.method == 'POST':
                if data=="admin":
                    body = request.json.get('username')
                    cur.execute("SELECT tempPass FROM users WHERE username=%s", (body,))
                    prenom = cur.fetchone()
                    return jsonify({"tempPass": prenom[0]})
                else:
                    return jsonify({"error": "Token invalide pour le post get possible"})
            elif request.method == 'GET':
                cur.execute("SELECT tempPass, lastChange FROM users WHERE username=%s", (data,))
                values = cur.fetchone()
                return jsonify({"tempPass": values[0], "lastChange": values[1]})

        