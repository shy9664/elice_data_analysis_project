from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    from models.user import User


    from blueprints.main import main
    from blueprints.login import login
    from blueprints.register import register
    
    app.register_blueprint(main)
    app.register_blueprint(login)
    app.register_blueprint(register)


    return app


if __name__ == '__main__' :
    create_app().run(debug=True)
