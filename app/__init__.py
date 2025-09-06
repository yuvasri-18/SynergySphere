from flask import Flask
from .extensions import db
from .routes import app as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    app.register_blueprint(main_blueprint)
    return app
