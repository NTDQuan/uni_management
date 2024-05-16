from model.Model import Major
from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine


def editMajor(majorID, major_data):
    """
    edit a major info
    arg:
        majorID(int) : major id to look for in database
        major_data(dict): contain new infomation to update
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    major = session.query(Major).get(majorID)
    major.major_name = major_data
    session.commit()
    session.close()

