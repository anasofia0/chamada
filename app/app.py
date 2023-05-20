from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import sqlite3

db: SQLAlchemy = SQLAlchemy()
bootstrap = Bootstrap5()

conn = sqlite3.connect("teste.db")


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "env"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///teste.db"

    # init
    db.init_app(app)
    bootstrap.init_app(app)

    from .auth.auth import bp

    app.register_blueprint(bp)

    return app


app = create_app()


# @app.route("/")
# def index():
#     return render_template("index.html")
