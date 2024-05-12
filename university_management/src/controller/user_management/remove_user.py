from database.initSession import session
from model.Model import User, Student, Lecturer



def deleteUser(userID: int) -> None:
    user = session.query(User).get(userID)
    print(user)
    if user:
        session.delete(user)
        session.commit()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {userID} not found")

def deleteStudent(userID: int) -> None:
    student = session.query(Student).get(userID)
    if student:
        session.delete(student)
        session.commit()
    else:
        print(f"Student with ID {userID} not found")

def deleteLecturer(userID: int):
    lecturer = session.query(Lecturer).get(userID)
    if lecturer:
        session.delete(lecturer)
        session.commit()
    else:
        print(f"Student with ID {userID} not found")