"""
@Author: Alice-Yuan
@File: adminService.py
@Time: 2024/09/16 14:51
"""
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select

from common.auth import auth_handler
from common.result import ResultModel
from exception.customException import UserNotFoundException, PasswordNotMatchException
from model import Session, get_db_session
from model.account import AccountLogin, AccountLoginResponse
from model.admin import AdminModel, Admin, AdminLoginResponse
from common.utils import set_attrs


class AdminService:
    @staticmethod
    def login(account: AccountLogin, db_session: Session) -> Admin:
        query = select(Admin).where(Admin.username == account.username)
        exist_admin: Admin = db_session.execute(query).scalars().first()
        if not exist_admin:
            raise UserNotFoundException('用户不存在')
        if not auth_handler.verify_password(account.password, exist_admin.password):
            raise PasswordNotMatchException('身份验证失败')

        account_login_response = AccountLoginResponse()
        set_attrs(account_login_response, jsonable_encoder(exist_admin))
        account_login_response.token = auth_handler.encode_token(exist_admin.id)
        return account_login_response
