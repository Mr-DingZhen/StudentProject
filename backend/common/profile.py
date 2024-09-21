"""
@Author: Alice-Yuan
@File: profile.py
@Time: 2024/09/20 14:11
"""
from pathlib import Path


class Profile:
    __file_path__ = None

    @staticmethod
    def get_files_path():
        project_path = Path(__file__).parent.parent  # 获取项目根目录
        file_path = project_path.joinpath("files")
        if not file_path.exists():
            file_path.mkdir(parents=True)
        Profile.__file_path__ = file_path
        return file_path
