from flask import Blueprint, render_template, redirect
from .form import RegisterForm, LoginForm
from ..app import db
from ..models.user import User  

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

        user = User(matricula = form.matricula,
                    nome = form.nome,
                    email = form.email,
                    professor = form.professor,
                    senha = form.senha # eu sei!!!!!
        )
        
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    
    return render_template("register.html", form=form)
