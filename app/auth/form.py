from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, Length


class RegisterForm(FlaskForm):
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
    submit = SubmitField("Criar usuário")


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
