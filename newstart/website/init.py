from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import secrets

db = SQLAlchemy()
csrf = CSRFProtect()   # 👈 CSRF object

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    app.config['SQLALCHEMY_BINDS'] = {
        'market': 'sqlite:///market.db',
        'marketItem': 'sqlite:///market_item.db'
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax' 
    app.config['SESSION_COOKIE_SECURE'] = False


    db.init_app(app)
    csrf.init_app(app)   # 👈 enable CSRF




    from .views import views
    from .auth import auth
    from .market import market
    from .account import account
    from .premium import premium
    
    app.register_blueprint(premium)
    app.register_blueprint(account)
    app.register_blueprint(market)
    app.register_blueprint(views)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
