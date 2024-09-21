"""
@Author: Alice-Yuan
@File: customException.py
@Time: 2024/09/16 14:59
"""


class CustomException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code


class UserNotFoundException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class UserExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class UserNameExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class PasswordNotMatchException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class TokenException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=401)


class CourseExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class CourseNotExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class FileNotFoundException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class StudentCourseExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class StudentCourseExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)


class StudentCourseNotExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)


class GradeExistException(CustomException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)
