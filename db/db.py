from flask_sqlalchemy import SQLAlchemy
from .config import Config
from app import get_app

db_config = Config()
app = get_app()
app.config['SQLALCHEMY_DATABASE_URI'] = db_config.get_uri()
_database = None

def get_database() -> SQLAlchemy:    
    global _database 
    if _database == None:
         _database = SQLAlchemy(app)
    return _database