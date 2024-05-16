from database.initSession import session
from model.Model import Student, Major, Gender, Lecturer
from sqlalchemy import or_, func, and_
from sqlalchemy.orm import sessionmaker

from university_management.src.controller.major_management.get_major import get_major_id
from university_management.src.database.Connect import engine
from university_management.src.util.getFirstAndLastName import getFirstAndLastName


def get_student_for_display_table(major_filter, gender_filter):
    """
    fetch student data to present in GUI
    args:
        major_filter(int): selected major id
        gender_filter(int): selected gender id
    return:
        result(list): contain all record
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    # Define columns to be selected
    columns = [Student.student_id, func.concat(Student.last_name, " ", Student.first_name).label("full_name"), Major.major_name, Gender.gender_name]

    # Define base query
    query = session.query(*columns).join(Major, Major.major_id == Student.major_id).join(Gender, Gender.gender_id == Student.gender_id)

    # Apply filters dynamically based on provided filter values
    if major_filter != "Ngành":
        query = query.filter(Major.major_name == major_filter)

    if gender_filter != "Giới tính":
        query = query.filter(Gender.gender_name == gender_filter)

    # Execute query and return result
    result = query.all()
    session.close()
    return result

def get_full_student_info(studentId):
    """
    get all column in major table
    arg:
        studentId(int): selected student id
    return:
        result(list): contain all info about selected student
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Student.student_id, Student.first_name, Student.last_name, Student.telephone, Student.address, Gender.gender_name, Major.major_name]
    query = session.query(*columns).join(Major, Major.major_id == Student.major_id).join(Gender, Gender.gender_id == Student.gender_id)
    query = query.filter(Student.student_id == studentId)
    result = query.first()
    session.close()
    return result


def search_student(input_query):
    """
    search for student with student id or student name
    args:
        input_query(str): query
    return:
        result(list): search result

    """
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Student.student_id, func.concat(Student.last_name, " ", Student.first_name).label("full_name"),
               Major.major_name, Gender.gender_name]

    query = session.query(*columns).join(Major, Major.major_id == Student.major_id).join(Gender, Gender.gender_id == Student.gender_id)

    query = query.filter(or_(Student.student_id == input_query, Student.first_name.like(input_query), Student.last_name.like(input_query), func.concat(Student.last_name, " ", Student.first_name).label("full_name") == input_query))

    result = query.all()
    session.close()
    return result

def get_lecturer_for_display_table(major_filter, gender_filter):
    """
    fetch lecturer data to present in GUI
    args:
        major_filter(int): selected major id
        gender_filter(int): selected gender id
    return:
        result(list): contain all record
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    # Define columns to be selected
    columns = [Lecturer.lecturer_id, func.concat(Lecturer.last_name, " ", Lecturer.first_name).label("full_name"), Major.major_name, Gender.gender_name]

    # Define base query
    query = session.query(*columns).join(Major, Major.major_id == Lecturer.major_id).join(Gender, Gender.gender_id == Lecturer.gender_id)

    # Apply filters dynamically based on provided filter values
    if major_filter != "Ngành":
        query = query.filter(Major.major_name == major_filter)

    if gender_filter != "Giới tính":
        query = query.filter(Gender.gender_name == gender_filter)

    # Execute query and return result
    result = query.all()
    session.close()
    return result

def get_full_lecturer_info(lecturerId):
    """
    get all column in lecturer table
    arg:
        lecturerId(int): selected lecturer id
    return:
        result(list): contain all info about selected lecturer
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Lecturer.lecturer_id, Lecturer.first_name, Lecturer.last_name, Lecturer.telephone, Lecturer.address, Gender.gender_name, Major.major_name]
    query = session.query(*columns).join(Major, Major.major_id == Lecturer.major_id).join(Gender, Gender.gender_id == Lecturer.gender_id)
    query = query.filter(Lecturer.lecturer_id == lecturerId)
    result = query.first()
    session.close()
    return result

def get_lecturer_id(lecturer_name):
    """
    convert lecturer name into lecturer id
    args:
        lecturer_name(str): lecturer name
    return:
        result.lecturer_id(int): lecturer id
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Get lecturer id...")
    last_name, first_name = getFirstAndLastName(lecturer_name)
    result = session.query(Lecturer).filter(and_(Lecturer.last_name == last_name, Lecturer.first_name == first_name)).first()
    print(result.lecturer_id)
    session.close()
    return result.lecturer_id

def get_all_lecturer():
    """
    get all lecturer name
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Lecturer).all()
    lecturer_list = []
    for row in result:
        lecturer_list.append(row.last_name + " " + row.first_name)
    session.close()
    return lecturer_list

def search_lecturer(input_query):
    """
    search for lecturer with lecturer id or lecturer name
    args:
        input_query(str): query
    return:
        result(list): search result

    """
    Session = sessionmaker(bind=engine)
    session = Session()
    columns = [Lecturer.lecturer_id, Lecturer.first_name, Lecturer.last_name, Lecturer.telephone, Lecturer.address, Gender.gender_name, Major.major_name]

    query = session.query(*columns).join(Major, Major.major_id == Lecturer.major_id).join(Gender, Gender.gender_id == Lecturer.gender_id)

    query = query.filter(or_(Lecturer.lecturer_id == input_query, Lecturer.first_name.like(input_query), Lecturer.last_name.like(input_query), func.concat(Lecturer.last_name, " ", Lecturer.first_name).label("full_name") == input_query))

    result = query.all()
    session.close()
    return result