"""
@Author: Alice-Yuan
@File: __init__.py.py
@Time: 2024/09/14 18:17
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}


origins = ["http://localhost:5173", "http://127.0.0.1:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from api import adminApi, courseApi, studentApi, fileApi, studentCourseApi, gradeApi, exceptionHandler
