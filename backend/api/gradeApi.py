"""
@Author: Alice-Yuan
@File: gradeApi.py
@Time: 2024/09/21 02:11
"""
from typing import Optional

from fastapi import APIRouter, Depends, Query

from api import app
from common.PageHelper import PageHelper
from common.result import ResultModel, Result
from model import Session, get_db_session
from model.grade import GradeCreate, GradeSearch, GradeUpdate
from service.gradeService import GradeService

grade_router = APIRouter(prefix='/grade')


@grade_router.post("/add", response_model=ResultModel)
async def add(grade_create: GradeCreate, db_session: Session = Depends(get_db_session)):
    GradeService.add_grade(grade_create, db_session)
    return Result.success()


@grade_router.get("/selectPage", response_model=ResultModel)
async def select_page(page: int = Query(1, ge=1, alias="pageNum", description="Page number"),
                      size: int = Query(5, gt=0, le=100, alias="pageSize", description="Page size"),
                      studentName: Optional[str] = Query(None, description="Student name"),
                      courseName: Optional[str] = Query(None, description="Course name"),
                      studentId: Optional[int] = Query(None, description="Student id"),
                      db_session: Session = Depends(get_db_session)):
    page_info = PageHelper.start_page(page, size)
    grade_search = GradeSearch(studentId=studentId, studentName=studentName, courseName=courseName)
    grade_list = GradeService.select_page(grade_search, db_session)
    return Result.success(data=page_info.of(grade_list))


@grade_router.put("/update", response_model=ResultModel)
async def update(grade_update: GradeUpdate, db_session: Session = Depends(get_db_session)):
    GradeService.update_by_id(grade_update, db_session)
    return Result.success()


@grade_router.delete("/delete/{id}", response_model=ResultModel)
async def delete(id: int, db_session: Session = Depends(get_db_session)):
    GradeService.delete_by_id(id, db_session)
    return Result.success()

app.include_router(grade_router)