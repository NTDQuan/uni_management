from database.initSession import session
from sqlalchemy import func, distinct, or_
from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Major, Student, Lecturer


def get_all_major():
    """
    get all major name
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Major).all()
    major_list = []
    for row in result:
        major_list.append(row.major_name)
    session.close()
    return major_list

def get_major_id(major_name):
    """
    conver major name into major id
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Get major id...")
    result = session.query(Major).filter(Major.major_name == major_name).first()
    print(result.major_id)
    session.close()
    return result.major_id

def get_major_for_display_table():
    """
    fetch major data to present in GUI
    """
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

def get_full_major_info(majorID):
    """
    get all column in major table
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Major.major_id, Major.major_name]
    query = session.query(*columns)
    result = query.filter(Major.major_id == majorID)
    session.close()
    return result

def search_major(input_query):
    """
    search for major with major id or major name
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Major.major_id, Major.major_name, func.count(distinct(Student.student_id)).label('num_students'), func.count(distinct(Lecturer.lecturer_id)).label('num_lecturers')]

    query = session.query(*columns).outerjoin(Student, Major.major_id == Student.major_id).outerjoin(Lecturer, Major.major_id == Lecturer.major_id).group_by(Major.major_id)

    query = query.filter(or_(Major.major_id.like(input_query), Major.major_name.like(input_query)))

    result = query.all()
    session.close()
    return result

