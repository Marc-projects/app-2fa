from flask import Flask, render_template, request, jsonify
import os, psycopg2, requests

app = Flask(__name__)

USER_APP = os.environ.get('USER_APP')
PASSWORD_APP = os.environ.get('PASSWORD_APP')
DB_APP = os.environ.get('DB_APP')
API_2FA = os.environ.get('API_2FA')
TOKEN_ADMIN = os.environ.get('TOKEN_ADMIN')


DATABASE_URL = f"postgresql://{USER_APP}:{PASSWORD_APP}@db:5432/{DB_APP}"

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.json.get('name')
    tempPass = request.json.get('pass')
    r = requests.post(API_2FA, headers = {"Authorization": TOKEN_ADMIN}, json={"username": name}, verify="ac.pem")
    response = r.json()
    if response["tempPass"] == tempPass:
        return jsonify({"result":"Good password !"})
    else:
        return jsonify({"result":"Wrong password"})
