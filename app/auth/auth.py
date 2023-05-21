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

        user = User(matricula = form.matricula.data,
                    nome = form.nome.data,
                    email = form.email.data,
                    professor = form.professor.data,
                    senha = form.senha.data # eu sei!!!!!
        )
        
        db.session.add(user)
        db.session.commit()
        created_user = User.query.filter_by(email=form.email.data).first()

        if created_user:
            print("User created successfully!")
            print("User details:", created_user)
        else:
            print("Failed to create user.")

        return redirect('/')
    
    return render_template("register.html", form=form)
