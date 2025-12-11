#svaki folder mora da ima fajl __init__.py

from app import create_app  #uvozimo ovu fju koja je u app/__init__.py

app = create_app()  #pravi Flask aplikaicju i registruje sve rute i ekstenzije

if __name__ == "__main__":
    app.run(debug=True) #pokrece ugradjeni Flask development server
                        #automatsko restartovanje pri promenama i ispis gresaka
