from sqlalchemy import or_
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

def get_course_id(course_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Get course id...")
    result = session.query(Course).filter(Course.course_name == course_name).first()
    print(result.course_id)
    session.close()
    return result.course_id

def get_all_course():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Course).all()
    course_list = []
    for row in result:
        course_list.append(row.course_name)
    session.close()
    return course_list

def search_course(input_query):
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Course.course_id, Course.course_name, Course.course_credit, Major.major_name]

    query = session.query(*columns).join(Major, Major.major_id == Course.major_id)

    query = query.filter(or_(Course.course_id.like(input_query), Course.course_name.like(input_query)))

    result = query.all()
    session.close()
    return result

