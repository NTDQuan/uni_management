from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Course


def editCourse(courseID, course_data):
    """
    Edit a course record
    Arg:
        courseID(int): course id for finding record
        course_data(dict): contain new info to update record
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    course = session.query(Course).get(courseID)
    if course:
        course.course_name = course_data["course_name"]
        course.course_credit = course_data["course_credit"]
        course.major_id = course_data["major"]
    session.commit()
    session.close()