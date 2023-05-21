from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os


db: SQLAlchemy = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'chamada.db')
    login_manager.init_app(app)
    app.config["SECRET_KEY"] = "env"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    # init
    db.init_app(app)
    with app.app_context():
        from .models.user import User
        db.create_all()
    bootstrap.init_app(app)

    from .auth.auth import bp

    app.register_blueprint(bp)

    return app


app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    from .models.user import User
    return User.query.get(user_id)
