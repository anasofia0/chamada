from flask import Blueprint, render_template, session, redirect
from .form import RegisterForm, LoginForm

bp = Blueprint("auth", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template("register.html", form=form)
