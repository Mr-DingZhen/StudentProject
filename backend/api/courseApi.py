"""
@Author: Alice-Yuan
@File: courseApi.py
@Time: 2024/09/17 15:59
"""
from typing import Optional

from fastapi import APIRouter, Depends, Query

from api import app
from common.PageHelper import PageHelper
from common.auth import auth_handler
from common.result import ResultModel, Result
from model import get_db_session, Session
from model.course import CourseSearch, CourseCreate, CourseUpdate
from service.courseService import CourseService

course_router = APIRouter(prefix='/course', dependencies=[Depends(auth_handler.auth_required)])


@course_router.get('/selectPage', response_model=ResultModel)
async def select_page(page: int = Query(1, gr=1, alias="pageNum", description="Page number"),
                      size: int = Query(5, gr=0, le=100, alias="pageSize", description="Page size"),
                      name: Optional[str] = Query(None, description="Course name"),
                      number: Optional[str] = Query(None, description="Course number"),
                      teacher: Optional[str] = Query(None, description="Teacher name"),
                      db_session: Session = Depends(get_db_session)):
    page_info = PageHelper.start_page(page, size)
    course_search = CourseSearch(name=name, number=number, teacher=teacher)
    course_list = CourseService.select_page(course_search, db_session)
    return Result.success(data=page_info.of(course_list))


@course_router.post('/add', response_model=ResultModel)
async def add(course_create: CourseCreate, db_session: Session = Depends(get_db_session)):
    CourseService.add_course(course_create, db_session)
    return Result.success()


@course_router.delete('/delete/{id}', response_model=ResultModel)
async def delete(id: int, db_session: Session = Depends(get_db_session)):
    CourseService.delete_by_id(id, db_session)
    return Result.success()


@course_router.put('/update', response_model=ResultModel)
async def update(course_update: CourseUpdate, db_session: Session = Depends(get_db_session)):
    CourseService.update_by_id(course_update, db_session)
    return Result.success()


app.include_router(course_router)
