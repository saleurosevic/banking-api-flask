from app.extensions import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False) # ovo je veza sa akaunt tabelom - jedna transakcija mora imati jedan akaunt, a jedan akaunt moze imati vise transakcija
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "account_id": self.account_id,
            "amount": self.amount,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }
