from database.initSession import session
from model.Model import Student, Major, Gender, Lecturer
from sqlalchemy import or_, func

from university_management.src.controller.major_management.get_major import get_major_id


def get_student_for_display_table(major_filter, gender_filter):
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

    return result

def get_full_student_info(studentId):
    columns = [Student.student_id, Student.first_name, Student.last_name, Student.telephone, Student.address, Gender.gender_name, Major.major_name]
    query = session.query(*columns).join(Major, Major.major_id == Student.major_id).join(Gender, Gender.gender_id == Student.gender_id)
    query = query.filter(Student.student_id == studentId)
    result = query.first()
    return result


def search_student(query_id):
    columns = [Student.student_id, func.concat(Student.last_name, " ", Student.first_name).label("full_name"),
               Major.major_name, Gender.gender_name]

    query = session.query(*columns).join(Major, Major.major_id == Student.major_id).join(Gender, Gender.gender_id == Student.gender_id)

    query = query.filter(Student.student_id == query_id)

    result = query.all()

    return result

def get_lecturer_for_display_table(major_filter, gender_filter):
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

    return result

def get_full_lecturer_info(lecturerId):
    columns = [Lecturer.lecturer_id, Lecturer.first_name, Lecturer.last_name, Lecturer.telephone, Lecturer.address, Gender.gender_name, Major.major_name]
    query = session.query(*columns).join(Major, Major.major_id == Lecturer.major_id).join(Gender, Gender.gender_id == Lecturer.gender_id)
    query = query.filter(Lecturer.lecturer_id == lecturerId)
    result = query.first()
    return result