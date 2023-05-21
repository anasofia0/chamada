from flask import Blueprint, render_template, redirect,request, url_for, flash
from flask_login import login_user
from .form import RegisterForm, LoginForm
from ..app import db
from ..models.user import User  

bp = Blueprint("auth", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        matricula = request.form.get("matricula")
        senha = request.form.get("senha")
        remember = True if request.form.get("remember") else False

        user = User.query.filter_by(matricula=matricula).first()

        if not user or not user.senha == senha:
            flash("Please check your login details and try again.")
            # Se não exisitir o usuário ou a senha estiver errada, redireciona para a página de login
            return redirect(url_for("auth.login"))

        # se passar no teste, faz o login e salva a sessão
        login_user(user, remember=remember)
        return render_template("loggedIn.html", user=user) # se o login for bem sucedido, redireciona para a dashboard
    return render_template("login.html")  

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        user = User(matricula = form.matricula.data,
                    nome = form.nome.data,
                    email = form.email.data,
                    professor = form.professor.data,
                    senha = form.senha.data # poderiamos usar um hash, mas como é algo simples, não vamos nos preocupar com isso
        )
        
        db.session.add(user)
        db.session.commit()
        created_user = User.query.filter_by(email=form.email.data).first()

        if created_user:
            print("User created successfully!")
            print("User details:", created_user)
        else:
            print("Failed to create user.")

        return redirect("/")
    
    return render_template("register.html", form=form)
