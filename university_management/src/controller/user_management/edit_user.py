from database.initSession import session
from model.Model import User, Student, Lecturer
from sqlalchemy.exc import IntegrityError

def studentUpdate(userID, user_data):
    """
    Edit a student record
    Arg:
        userID(int): student id for finding record
        user_data(dict): contain new info to update record
    """
    user = session.query(User).get(userID)
    user.email = user_data["new_email"]
    student = session.query(Student).get(userID)
    student.student_id = int(user_data["new_id"])
    student.first_name = user_data["new_first_name"]
    student.last_name = user_data["new_last_name"]
    student.telephone = user_data["new_telephone"]
    student.address = user_data["new_address"]
    student.gender_id = user_data["new_gender"]
    student.major_id = user_data["new_major"]
    session.commit()

def lecturerUpdate(userID, user_data):
    """
    Edit a lecturer record
    Arg:
        userID(int): lecturer id for finding record
        user_data(dict): contain new info to update record
    """
    user = session.query(User).get(userID)
    user.email = user_data["new_email"]
    lecturer = session.query(Lecturer).get(userID)
    lecturer.lecturer_id = int(user_data["new_id"])
    lecturer.first_name = user_data["new_first_name"]
    lecturer.last_name = user_data["new_last_name"]
    lecturer.telephone = user_data["new_telephone"]
    lecturer.address = user_data["new_address"]
    lecturer.gender_id = user_data["new_gender"]
    lecturer.major_id = user_data["new_major"]
    session.commit()

def editStudent(userID, user_data):
    """
    implement
    """
    try:
        # Update student record first
        studentUpdate(userID, user_data)
        session.commit()

    except IntegrityError as e:
        session.rollback()
        raise e  # Re-raise the exception

def editLecturer(userID, user_data):
    """
    implement
    """
    try:
        lecturerUpdate(userID, user_data)
        session.commit()

    except IntegrityError as e:
        session.rollback()
        raise e

