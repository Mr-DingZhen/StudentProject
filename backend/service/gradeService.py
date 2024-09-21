"""
@Author: Alice-Yuan
@File: gradeService.py
@Time: 2024/09/21 02:11
"""
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, and_, asc

from common.utils import set_attrs
from exception.customException import GradeExistException
from model import Session
from model.course import Course
from model.grade import GradeCreate, GradeSearch, GradeUpdate, Grade
from model.student import Student


class GradeService:
    @staticmethod
    def add_grade(grade: GradeCreate, db_session: Session):
        query = select(Grade).where(and_(Grade.studentId == grade.studentId, Grade.courseId == grade.courseId))
        exist_grade: Grade = db_session.execute(query).scalar()
        if exist_grade:
            raise GradeExistException("成绩已存在")
        new_grade = Grade()
        set_attrs(new_grade, jsonable_encoder(grade))
        db_session.add(new_grade)
        db_session.commit()
        return new_grade

    @staticmethod
    def select_page(grade: GradeSearch, db_session: Session):
        query = select(Grade, Student, Course).outerjoin(Grade.student).outerjoin(Grade.course).order_by(asc(Grade.id))
        if grade.studentName:
            query = query.where(Student.name.like(f"%{grade.studentName}%"))
        if grade.courseName:
            query = query.where(Course.name.like(f"%{grade.courseName}%"))
        if grade.studentId:
            query = query.where(Grade.studentId == grade.studentId)
        result = db_session.execute(query).scalars().all()
        return result

    @staticmethod
    def update_by_id(grade: GradeUpdate, db_session: Session):
        query = select(Grade).where(Grade.id == grade.id)
        exist_grade: Grade = db_session.execute(query).scalar()
        if not exist_grade:
            raise GradeExistException("成绩记录不存在")
        set_attrs(exist_grade, jsonable_encoder(grade))
        db_session.commit()
        return exist_grade

    @staticmethod
    def delete_by_id(id: int, db_session: Session):
        exist_grade: Grade = check_grade_exist(id, db_session)
        db_session.delete(exist_grade)
        db_session.commit()
        return exist_grade


def check_grade_exist(grade_id: int, db_session: Session):
    query = select(Grade).where(Grade.id == grade_id)
    exist_grade: Grade = db_session.execute(query).scalar()
    if not exist_grade:
        raise GradeExistException("成绩记录不存在")
    return exist_grade
