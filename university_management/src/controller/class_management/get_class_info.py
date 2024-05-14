from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Class, Lecturer, Course


def get_class_for_display_table():
    Session = sessionmaker(bind=engine)
    session = Session()

    columns = [Class.class_id, Class.class_name, Class.semester, Class.year, func.concat(Lecturer.last_name, " ", Lecturer.first_name).label("full_name"), Course.course_name, Class.status, Class.start_period, Class.end_period, Class.day]

    query = session.query(*columns).join(Lecturer, Lecturer.lecturer_id == Class.lecturer_id).join(Course, Course.course_id == Class.course_id)

    result = query.all()
    session.close()
    return result

def get_full_class_info(classId):
    Session = sessionmaker(bind=engine)
    session = Session()

    columns = [Class.class_id, Class.class_name, Class.semester, Class.year, func.concat(Lecturer.last_name, " ", Lecturer.first_name).label("full_name"), Course.course_name, Class.status, Class.start_period, Class.end_period, Class.day]

    query = session.query(*columns).join(Lecturer, Lecturer.lecturer_id == Class.lecturer_id).join(Course, Course.course_id == Class.course_id)
    query = query.filter(Class.class_id == classId)
    result = query.first()
    session.close()
    return result