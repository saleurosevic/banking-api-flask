from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.account import Account
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

accounts_bp = Blueprint("accounts", __name__)  # grupu ruta sa /accounts

@accounts_bp.get("/") # kada nam sa fronta stigne get zahtev na putanji accounts pozivamo ovu metodu
@jwt_required(optional=True)   # dozvoljava anonimni pregled, ruta je dostupna SVIMA, ne gleda se token
def list_accounts():
    accounts = Account.query.all() # vraca sve iz tabele Account
    return jsonify([a.to_dict() for a in accounts])

@accounts_bp.post("/")
@jwt_required() # potreban token da bude validan
def create_account():
    data = request.json or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "name required"}), 400

    user_id = get_jwt_identity()    # da bi neko napravio akaunt on mora vec biti ulogovan i njegov id je u tokenu i ovako samo desifrovanjem tokena dohvatamo njegov user_id
                                    # ovome smo mogli mozda da pristupimo i preko session[user_id]

    account = Account(owner_id=user_id, name=name, balance=0.0) # kreiramo novi redu Accountu
    db.session.add(account)
    db.session.commit()
    return jsonify(account.to_dict()), 201

@accounts_bp.get("/<int:account_id>") # ovo je dinamicki parametar, i postoji vise razlicitih linkova sa njim npr /accounts/1 ili /accounts/38 i on ovaj dinamicki account_id salje do ove metode
@jwt_required() # potreban token
def get_account(account_id):
    account = Account.query.get_or_404(account_id) # dohvati ovaj account ako ima, ako ne vrati error 404 not found
    return jsonify(account.to_dict())
