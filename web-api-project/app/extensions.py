#uvozimo ove flask ekstenzije
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()   # kreira instancu SQLAlchemy i kasnije se povezuje u init sa app preko init_app(),
                    # omogucava nam da pisemo pajton kod i on ga automatski pretvara u sql i to je ORM(Object Relational Mapper)

migrate = Migrate() # Flask-Migrate, za razne promene u bazi

jwt = JWTManager()  # Flask-JWT-Extended, za rad sa tokenima
