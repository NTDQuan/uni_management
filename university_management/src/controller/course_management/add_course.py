from model.Model import Course

from university_management.src.database.initSession import session


def add_course(course_data: dict):
    course = Course(course_name = course_data["course_name"], course_credit = course_data["course_credit"], major_id = course_data["major_id"])
    session.add(course)
    session.commit()