from model.Model import Course
from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.database.initSession import session


def add_course(course_data: dict):
    """
    Add new course to the database
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    course = Course(course_id = course_data["course_id"], course_name = course_data["course_name"], course_credit = course_data["course_credit"], major_id = course_data["major_id"])
    session.add(course)
    session.commit()
    session.close()