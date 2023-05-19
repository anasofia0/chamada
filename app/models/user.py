from . import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[String] = mapped_column(String(50))
    email: Mapped[String] = mapped_column()
    professor: Mapped[Boolean] = mapped_column()
