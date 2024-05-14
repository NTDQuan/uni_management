from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Class


def editClass(classID, class_data):
    Session = sessionmaker(bind=engine)
    session = Session()
    selected_class = session.query(Class).get(classID)
    if selected_class:
        selected_class.class_name = class_data["class_name"]
        selected_class.semester = class_data["semester"]
        selected_class.year = class_data["year"]
        selected_class.lecturer_id = class_data["lecturer_id"]
        selected_class.course_id = class_data["course_id"]
        selected_class.start_period = class_data["start_period"]
        selected_class.end_period = class_data["end_period"]
        selected_class.day = class_data["day"]
    session.commit()
    session.close()