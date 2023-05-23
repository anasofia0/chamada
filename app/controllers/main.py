from flask import Blueprint, render_template
from flask_login import login_user
form ..models import User

bp = Blueprint('main',__name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")    

@bp.route('/home', methods=['GET'])
def home():
    # if login_user.current_user
    # nao vou mentir, eu to bem perdida
    return render_template("home.html", user=None)