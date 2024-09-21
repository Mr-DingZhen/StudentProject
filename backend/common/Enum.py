"""
@Author: Alice-Yuan
@File: Enum.py
@Time: 2024/09/19 14:43
"""
from enum import Enum


class Role(str, Enum):
    ADMIN = "管理员"
    STUDENT = "学生"
