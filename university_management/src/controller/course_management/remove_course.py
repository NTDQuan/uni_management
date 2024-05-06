from database.initSession import session
from model.Model import Course

def delete_course(courseID: int) -> None:
    user = session.query(Course).get(courseID)
    print(user)
    if user:
        session.delete(user)
        session.commit()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {courseID} not found")