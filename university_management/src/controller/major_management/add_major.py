from university_management.src.database.initSession import session
from university_management.src.model.Model import Major


def add_major(major_data: dict):
    major = Major(major_id = major_data["major_id"], major_name = major_data["major_name"])
    session.add(major)
    session.commit()