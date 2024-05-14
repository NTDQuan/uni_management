from database.initSession import session
from sqlalchemy import func, distinct
from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Major, Student, Lecturer


def get_all_major():
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Major).all()
    major_list = []
    for row in result:
        major_list.append(row.major_name)
    session.close()
    return major_list

def get_major_id(major_name):
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Get major id...")
    result = session.query(Major).filter(Major.major_name == major_name).first()
    print(result.major_id)
    session.close()
    return result.major_id

def get_major_for_display_table():
    Session = sessionmaker(bind=engine)
    session = Session()
    # Define columns to be selected
    columns = [Major.major_id, Major.major_name, func.count(distinct(Student.student_id)).label('num_students'), func.count(distinct(Lecturer.lecturer_id)).label('num_lecturers')]

    # Define base query
    query = session.query(*columns).outerjoin(Student, Major.major_id == Student.major_id).outerjoin(Lecturer, Major.major_id == Lecturer.major_id).group_by(Major.major_id)

    # Execute query and return result
    result = query.all()
    session.close()

    return result

def get_full_major_info():
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Major.major_id, Major.major_name]
    query = session.query(*columns)
    result = query.first()
    session.close()
    return result

