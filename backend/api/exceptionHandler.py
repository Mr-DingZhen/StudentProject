"""
@Author: Alice-Yuan
@File: exceptionHandler.py
@Time: 2024/09/16 15:01
"""
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from fastapi import Request
from api import app
from common.result import Result
from exception.customException import UserNotFoundException, PasswordNotMatchException, TokenException, \
    CourseExistException, CourseNotExistException, UserExistException, FileNotFoundException, \
    StudentCourseExistException, StudentCourseNotExistException, GradeExistException, CustomException


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    result = Result.error(code=exc.status_code, msg=exc.message)
    return JSONResponse(status_code=exc.status_code, content=jsonable_encoder(result))



