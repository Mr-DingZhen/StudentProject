"""
@Author: Alice-Yuan
@File: adminApi.py
@Time: 2024/09/16 14:47
"""
from fastapi import Depends, Body
from fastapi.encoders import jsonable_encoder

from api import app
from common.Enum import Role
from common.result import ResultModel, Result
from model import Session, get_db_session
from model.account import AccountLogin
from model.admin import AdminModel
from service.adminService import AdminService
from service.studentService import StudentService


@app.post('/login', response_model=ResultModel)
async def login(account: AccountLogin, db_session: Session = Depends(get_db_session)):
    if Role.ADMIN.name.__eq__(account.role):
        db_account = AdminService.login(account, db_session)
    elif Role.STUDENT.name.__eq__(account.role):
        db_account = StudentService.login(account, db_session)
    else:
        return Result.error("角色不存在")
    return Result.success(data=jsonable_encoder(db_account))
