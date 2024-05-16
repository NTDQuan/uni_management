from database.initSession import session
from model.Model import Course

def delete_course(courseID: int) -> None:
    """
    delete course from database
    args:
        courseID(int)
    """
    course = session.query(Course).get(courseID)
    print(course)
    if course:
        session.delete(course)
        session.commit()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {courseID} not found")