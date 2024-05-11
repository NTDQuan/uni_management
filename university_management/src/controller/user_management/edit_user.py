from database.initSession import session
from model.Model import User, Student
from sqlalchemy.exc import IntegrityError


def userUpdate(userID, user_data):
    user = session.query(User).get(userID)
    user.email = user_data["new_email"]
    session.commit()

def studentUpdate(userID, user_data):
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

def editStudent(userID, user_data):
    new_user_id = int(user_data["new_id"])
    try:
        # Update student record first
        studentUpdate(userID, user_data)
        session.commit()

    except IntegrityError as e:
        session.rollback()
        raise e  # Re-raise the exception

