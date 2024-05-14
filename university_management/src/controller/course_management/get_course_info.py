from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Course, Major


def get_course_for_display_table():
    Session = sessionmaker(bind=engine)
    session = Session()

    columns = [Course.course_id, Course.course_name, Course.course_credit, Major.major_name]

    query = session.query(*columns).join(Major, Major.major_id == Course.major_id)

    result = query.all()
    session.close()
    return result

def get_full_course_info(courseId):
    Session = sessionmaker(bind=engine)
    session = Session()

    columns = [Course.course_id, Course.course_name, Course.course_credit, Major.major_name]

    query = session.query(*columns).join(Major, Major.major_id == Course.major_id)
    query = query.filter(Course.course_id == courseId)
    result = query.first()
    session.close()
    return result

