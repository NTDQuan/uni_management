from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.database.initSession import session
from university_management.src.model.Model import Major


def add_major(major_data: dict):
    """
    adđ new major to database
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    major = Major(major_id = major_data["major_id"], major_name = major_data["major_name"])
    session.add(major)
    session.commit()
    session.close()