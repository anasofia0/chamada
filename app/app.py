from flask import Flask, render_teamplate
from flask_bootstrap import Bootstrap5

def create_app(config_filename):
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    
    # app.config.from_pyfile(config_filename)

    # init 
    # db = SQLAlchemy() colocar isso na model
    # from yourapplication.model import db
    # db.init_app(app)


    # from yourapplication.views.admin import admin
    # from yourapplication.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)

    return app