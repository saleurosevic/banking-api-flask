from app.extensions import db

class Account(db.Model):
    __tablename__ = "accounts"

    #kolone
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) #veza sa tabelom users i kolonom id odatle, svaki account mora imati usera
    name = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    owner = db.relationship("User", backref=db.backref("accounts", lazy=True))  # veza izmedju Account i User
                                                                                # ovo backref znaci da i u User ima atribut accounts
                                                                                # lazy = True - ne ucitava se odmah vec tek sa direktnim zahtevom za ovo
                                                                                # Account.owner - dobijamo Usera
                                                                                # User.accounts - dobijamo listu akaunta za ovog Usera

    transactions = db.relationship("Transaction", backref="account", lazy=True) # veza izmedju Account i Transaction
                                                                                # Account.transactions - vraca listu transakcija za ovaj akaunt
                                                                                # Transaction.account - vraca akaunt koji je izvrsio ovu transakciju
                                                                                # ko vraca listu a ko jednog zavisi iskljucivo od FOREIGN KEY-a

    # za ispis ovog objekta
    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "balance": self.balance,
            "transactions": [t.to_dict() for t in self.transactions]
        }
