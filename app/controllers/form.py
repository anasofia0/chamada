from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp, Length


class RegisterForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    matricula = StringField(
        "matricula",
        validators=[
            DataRequired(),
            Regexp("\d", message="Matrícula deve conter somente digitos numéricos"),
        ],
    )
    email = StringField(
        "email",
        validators=[DataRequired(), Email(message="Inserir endereço de e-mail válido")],
    )
    senha = PasswordField(
        validators=[
            DataRequired(),
            Length(6, 20, message="Senhas com no mínimo 6 caracteres e máximo 20"),
        ]
    )
    submit = SubmitField("Submeter formulário")


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
