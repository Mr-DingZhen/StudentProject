"""
@Author: Alice-Yuan
@File: courseService.py
@Time: 2024/09/17 16:01
"""
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, desc

from common.utils import set_attrs
from exception.customException import CourseExistException, CourseNotExistException
from model import Session
from model.course import Course, CourseSearch, CourseCreate, CourseUpdate


class CourseService:
    @staticmethod
    def select_page(course_search: CourseSearch, db_session: Session):
        query = select(Course).order_by(desc(Course.id))
        if name := course_search.number:
            query = query.where(Course.name.like(f'%{name}%'))
        if number := course_search.number:
            query = query.where(Course.number.like(f'%{number}%'))
        if teacher := course_search.teacher:
            query = query.where(Course.teacher.like(f'%{teacher}%'))
        result = db_session.execute(query).scalars().all()
        return result

    @staticmethod
    def add_course(course_create: CourseCreate, db_session: Session):
        query = select(Course).where(Course.name == course_create.name)
        exist_course: Course = db_session.execute(query).scalars().all()
        if exist_course:
            raise CourseExistException("课程名已存在")
        course = Course(**course_create.dict())
        db_session.add(course)
        db_session.commit()
        return course

    @staticmethod
    def update_by_id(course: CourseUpdate, db_session: Session):
        exist_course: Course = check_course_exist(course.id, db_session)
        set_attrs(exist_course, jsonable_encoder(course))
        db_session.commit()
        return exist_course

    @staticmethod
    def delete_by_id(id: int, db_session: Session):
        exist_course: Course = check_course_exist(id, db_session)
        db_session.delete(exist_course)
        db_session.commit()
        return exist_course


def check_course_exist(course_id: int, db_session: Session):
    query = select(Course).where(Course.id == course_id)
    exist_course: Course = db_session.execute(query).scalar()
    if not exist_course:
        raise CourseNotExistException("课程不存在")
    return exist_course
