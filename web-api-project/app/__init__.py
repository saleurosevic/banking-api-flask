from flask import Flask
from app.config import Config   #ovo je moja klasa iz config.py
from app.extensions import db, migrate, jwt #uvozi ove neke ekstenzije

def create_app():  #funkcija koja pravi i konfigurise aplikaciju
    #kreiranje flask aplikacije
    app = Flask(__name__)

    # Init configurations
    app.config.from_object(Config) #uvozi konfiguraciju iz ove klase, uzima sve UPPERCASE promenljvie i ubacuje ih u konfiguraciju
                                   #SECRET_KEY - za zastitu, kripciju npr

    # Init extensions
    db.init_app(app) #povezuje instancu baze sa aplikacijom
    migrate.init_app(app, db) #povezuje flask-migrate sa aplikacijom i instancom baze, kasnije koristimo flask db komande za migraciju
    jwt.init_app(app) #povezuje flask-jwt-extended sa aplikacijom

    # Register blueprints (routes)
    #uvozimo ove nase blueprintove(odeljke) i posle im dole dodeljujemo putanju do njih i u svakom od ova 3 odeljka imamo kao pod odeljke
    from app.routes.auth import auth_bp
    from app.routes.accounts import accounts_bp
    from app.routes.transactions import transactions_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(accounts_bp, url_prefix="/accounts")
    app.register_blueprint(transactions_bp, url_prefix="/transactions")

    @app.route("/")  #ovo mi je moja pocetna ruta, ovo se pojavljuje na pocetnom linku
    def home():
        return {"message": "Banking API Flask + SQLAlchemy"} #vraca ovu JSON poruku vidljivu na ovom linku

    return app #vraca u run.py odakle i pozivamo ovaj program ovu nasu aplikaciju
