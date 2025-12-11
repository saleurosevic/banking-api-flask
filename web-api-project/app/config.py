import os  #ovo je modul za rad sa env varijablama i putanjama
from dotenv import load_dotenv

#.env je obican tekst fajl u kome se cuvaju osetljivi podaci i obicno su svi oblika KEY = VALUE
# učitaj .env ako postoji i postavlja varijable u okruzenje, jer lozinke i URL cuvamo u .env
load_dotenv()

#klasa koja definise konfiguraciju
class Config:
    #.getenv(variabla, def_value) smesta vrednost za ovu variablu u nasu variablu, ako ne postoji u env fajlu dodeljujemo joj ovaj drugi argument
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey") #ovo je neki tajni kljuc koji se koristi u flasku za sesije, CSRF,... i cuva se u env
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dev.db")  # za razvoj koristimo sqlite; kasnije ćemo promeniti DATABASE_URL na postgres
    SQLALCHEMY_TRACK_MODIFICATIONS = False #promena nekih modela nmp samo iskljucli bzvz

    # JWT(json web token) - da backend zna ko je koristi bez da cuva podatke o njemu u memoriji, server zna ko je korisnik i sta sme da radi
    # cuvaju se obicno u browseru u local storage ili cookie
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-string")
