from database.initSession import session
from model.Model import Student, Major, Gender
from sqlalchemy import or_, func

from university_management.src.controller.major_management.get_major import get_major_id


def get_student_for_display_table(major_filter, gender_filter):
    # Define columns to be selected
    columns = [Student.student_id, func.concat(Student.first_name, " ", Student.last_name).label("full_name"), Major.major_name, Gender.gender_name]

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

def search_student(query_id):
    columns = [Student.student_id, func.concat(Student.first_name, " ", Student.last_name).label("full_name"),
               Major.major_name, Gender.gender_name]

    query = session.query(*columns).join(Major, Major.major_id == Student.major_id).join(Gender, Gender.gender_id == Student.gender_id)

    query = query.filter(Student.student_id == query_id)

    result = query.all()

    return result