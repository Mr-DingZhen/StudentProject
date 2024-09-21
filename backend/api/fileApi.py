"""
@Author: Alice-Yuan
@File: fileApi.py
@Time: 2024/09/20 14:04
"""
import mimetypes
from datetime import datetime

from fastapi import APIRouter, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
from api import app
from common.constant import PORT, HOST
from common.profile import Profile
from common.result import ResultModel, Result
from werkzeug.utils import secure_filename

from exception.customException import FileNotFoundException

file_router = APIRouter(prefix='/files')


@file_router.post("/upload", response_model=ResultModel)
async def upload(file: UploadFile):
    original_filename = secure_filename(file.filename)
    timestamp = int(datetime.now().timestamp())
    unique_filename = f"{timestamp}_{original_filename}"
    file_save_path = Profile.get_files_path()
    # 保存文件路径
    file_final_path = file_save_path.joinpath(unique_filename)
    # 保存文件
    with open(file_final_path, 'wb') as buffer_file:
        content = await file.read()
        buffer_file.write(content)
    # 返回文件下载路径
    url = f"http://{HOST}:{PORT}/files/download?filename={unique_filename}"
    return Result.success(data=jsonable_encoder({"url": url}))


@file_router.get("/download", response_model=ResultModel)
async def download(filename: str):
    file_save_path = Profile.get_files_path()
    file_path = file_save_path.joinpath(filename)
    if not file_path.exists():
        raise FileNotFoundException("文件不存在")
    mime_type, _ = mimetypes.guess_type(file_path)
    # 创建文件流响应，以便流式传输文件，同时设置文件类型
    response = StreamingResponse(open(file_path, 'rb'), media_type=mime_type)
    # 不设置Content-Disposition，避免浏览器直接下载
    return response


app.include_router(file_router)
