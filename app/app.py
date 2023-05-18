from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db:SQLAlchemy = SQLAlchemy()
bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)

    # init
    db.init_app(app)
    bootstrap.init_app(app)

    from .controllers import blueprints
    app.register_blueprint(blueprints())

    return app


app = create_app()


# @app.route("/")
# def index():
#     return render_template("index.html")
