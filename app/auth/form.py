from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError
from wtforms.validators import Optional


class ProfessorCodeCheck:
    def __init__(self, message=None):
        if not message:
            message = "Incorrect code provided"
        self.message = message

    def __call__(self, form, field):
        if form.professor.data and (not field.data or field.data != 'debugmode'):
            raise ValidationError(self.message)


class RegisterForm(FlaskForm):
    # Your existing fields...
    nome = StringField("Nome", validators=[DataRequired()])
    matricula = StringField(
        "Matricula",
        validators=[
            DataRequired(),
            Regexp("\d", message="Matrícula deve conter somente digitos numéricos"),
        ],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(message="Inserir endereço de e-mail válido")],
    )
    senha = PasswordField(
        "Senha",
        validators=[
            DataRequired(),
            Length(6, 20, message="Senhas com no mínimo 6 caracteres e máximo 20"),
        ]
    )
    professor = BooleanField("Professor")
    professor_code = StringField("Code for Professor", [Optional(), ProfessorCodeCheck()])
    submit = SubmitField("Criar usuário")



class ProfessorCodeCheck:
    def __init__(self, message=None):
        if not message:
            message = "Incorrect code provided"
        self.message = message

    def __call__(self, form, field):
        if form.professor.data and field.data != 'debugmode':
            raise ValidationError(self.message)

class LoginForm(FlaskForm):
    matricula = StringField(
        "matricula",
        validators=[
            DataRequired(),
            Regexp("\d", message="Matrícula deve conter somente digitos numéricos"),
        ],
    )
    senha = PasswordField(
        validators=[
            DataRequired(),
            Length(
                min=6, max=20, message="Senhas com no mínimo 6 caracteres e máximo 20"
            ),
        ]
    )
