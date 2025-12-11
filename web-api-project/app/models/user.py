from app.extensions import db  #ona SQLAlchemy instanca sto smo ranije napravili da moze python u sql kod
from werkzeug.security import generate_password_hash, check_password_hash # za hesiranje lozinki
from datetime import datetime

class User(db.Model): #prosledjujemo uvek ovaj parametar nasoj klasi koja nam predstavlja tabelu u bazi i omogucava da koristimo ovo column, string,...
    __tablename__ = "users" #ovo je naziv tabele u bazi

    #definicija kolona
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    #ovde kreiramo i ove pomocne metode za rad sa nasim kolonama, u ovom slucaju sa password
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_dict(self): #metoda koja vraca prikaz korisnika
        return {"id": self.id, "username": self.username}
