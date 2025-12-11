from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.account import Account
from app.models.transaction import Transaction
from flask_jwt_extended import jwt_required, get_jwt_identity

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.post("/<int:account_id>") # ponovo dimanicki link, znamo ko nam je ulogovan
@jwt_required()
def add_transaction(account_id):
    account = Account.query.get_or_404(account_id) # get trazi iskljucivo po primary key, a filter by po bilo kojoj koloni koju mi stavimo
    data = request.json or {}
    amount = data.get("amount")
    description = data.get("description", "")

    if amount is None:
        return jsonify({"error": "amount is required"}), 400

    tx = Transaction(account_id=account.id, amount=float(amount), description=description)
    account.balance += float(amount)
    db.session.add(tx)
    db.session.commit() # commit sluzi da promeni u bazi sve promene koje su nastale i na nasim pajton objektima klasa, ovde npr za account.balance ne samo za ove db.session....
    return jsonify(tx.to_dict()), 201
