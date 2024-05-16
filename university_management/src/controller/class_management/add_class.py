from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.database.initSession import session
from model.Model import Class

def add_class(class_data: dict):
    """
    Add new class to database

    Args:
        class_data: dictionary
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    new_class = Class(class_id = class_data["class_id"], class_name = class_data["class_name"], semester = class_data["semester"], year = class_data["year"], lecturer_id = class_data["lecturer_id"], course_id = class_data["course_id"], status = class_data["status"], start_period = class_data["start_period"], end_period = class_data["end_period"], day = class_data["day"])
    session.add(new_class)
    session.commit()
    session.close()