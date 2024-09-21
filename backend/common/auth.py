"""
@Author: Alice-Yuan
@File: auth.py
@Time: 2024/09/17 15:09
"""
from datetime import datetime, timedelta

import jwt
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext

from common.constant import TOKEN_EXPIRE_DAYS, TOKEN_EXPIRE_MINUTES, TOKEN_EXPIRE_SECONDS


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"

    def get_password_hash(self, password):
        """
        加密密码
        :param password: 明文密码
        :return: 加密后的密码
        """
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        """
        验证密码
        :param plain_password: 明文密码
        :param hashed_password: 加密密码
        :return: 密码是否匹配
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id: int):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=TOKEN_EXPIRE_DAYS,
                                                 minutes=TOKEN_EXPIRE_MINUTES,
                                                 seconds=TOKEN_EXPIRE_SECONDS),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, self.secret, algorithm='HS256')

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'token过期'
        except jwt.InvalidTokenError:
            return 'token无效'

    def auth_required(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


auth_handler = AuthHandler()
