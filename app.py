from flask import Flask

_app = None

def get_app():
    global _app
    if _app == None:
        _app = Flask(__name__)
        _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return _app