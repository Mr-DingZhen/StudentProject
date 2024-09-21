"""
@Author: Alice-Yuan
@File: account.py
@Time: 2024/09/19 14:38
"""
from pydantic import BaseModel


class AccountLogin(BaseModel):
    username: str
    password: str
    role: str


class AccountLoginResponse:
    id: int
    username: str
    name: str
    role: str
    token: str


class AccountRegister(BaseModel):
    username: str
    password: str
