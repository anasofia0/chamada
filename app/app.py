from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    app.config.from_prefixed_env()


    # app.config.from_pyfile(config_filename)

    # init
    # db = SQLAlchemy() colocar isso na model
    # from yourapplication.model import db
    # db.init_app(app)

    from .controllers import blueprints
    app.register_blueprint(blueprints())




    return app


app = create_app()


# @app.route("/")
# def index():
#     return render_template("index.html")
