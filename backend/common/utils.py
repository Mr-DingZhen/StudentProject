"""
@Author: Alice-Yuan
@File: utils.py
@Time: 2024/09/18 15:13
"""


def set_attrs(obj, data: dict):
    if data:
        for key, value in data.items():
            setattr(obj, key, value)

