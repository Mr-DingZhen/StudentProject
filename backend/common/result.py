"""
@Author: Alice-Yuan
@File: result.py
@Time: 2024/09/14 18:07
"""
from pydantic import BaseModel


class ResultBase:
    code: str
    msg: str
    data: dict


class ResultModel(BaseModel, ResultBase):
    pass


class Result(ResultBase):

    def __init__(self, code: str, msg: str, data: object):
        self.code = code
        self.msg = msg
        self.data = data

    @classmethod
    def success(cls, code: str = "200", msg: str = "success", data: object = None):
        if not data:
            data = {}
        return cls(code=code, msg=msg, data=data)

    @classmethod
    def error(cls, code: str = "500", msg: str = "error", data: object = None):
        if not data:
            data = {}
        return cls(code=code, msg=msg, data=data)
