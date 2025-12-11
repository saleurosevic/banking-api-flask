from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)  # putanja do ovog odeljka je /auth

@auth_bp.post("/register")  # putanja koja prima POST zahtev na /auth/register
def register():
    data = request.json or {}  # dohvata podatke koji su poslati kroz JSON u HTTP requestu, ako ne sadrzi json onda je {} ovo uvek pisi zbog greski
                               # ovaj data dobijamo iz front dela aplikacije

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400 # salje odgovor klijentu i vraca HTTP status kod 400 - Bad Request

    if User.query.filter_by(username=username).first(): # trazi da li postoji username u bazi sa ovim imenom, ako postoji - greska
        return jsonify({"error": "username already exists"}), 400

    user = User(username=username)  # kreiramo objekat User - zapravo novi red u nasoj tabeli users
    user.set_password(password) # pozivamo funkciju za hesiranje lozinke
    db.session.add(user) # dodajemo korisnika u bazu
    db.session.commit()
    return jsonify(user.to_dict()), 201  # vraca ispis usera i HTTP kod 201 (created)

@auth_bp.post("/login") # putanja koja prima POST zahtev na /auth/login
def login():
    data = request.json or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    user = User.query.filter_by(username=username).first()  # trazi u bazi u tabeli User red sa ovim username
    if not user or not user.check_password(password): # ako ne postoji user ili ako postoji ali mu lozinka nije dobra
        return jsonify({"error": "invalid credentials"}), 401

    token = create_access_token(identity=user.id)  # identity = user.is pripada ovom useru samo
    return jsonify({"access_token": token}) # ovo saljemo frontendu i on to posle cuva u local storage-u
