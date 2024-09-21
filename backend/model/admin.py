"""
@Author: Alice-Yuan
@File: admin.py
@Time: 2024/09/16 14:41
"""
import bcrypt
from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from model import Base


class Admin(Base):
    __tablename__ = 'admin'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(255), nullable=False)

    def password_check(self, password):
        return bcrypt.checkpw(password.encode(), self.password.encode())


class AdminModel(BaseModel):
    username: str
    password: str


class AdminLoginResponse(BaseModel):
    id: int
    username: str
    token: str


