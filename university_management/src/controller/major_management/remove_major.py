from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.database.initSession import session
from university_management.src.model.Model import Major


def delete_major(majorID: int) -> None:
    """
    delete major from database
    args:
        majorID(int): major id to be removed
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    major = session.query(Major).get(majorID)
    print(major)
    if major:
        session.delete(major)
        session.commit()
        session.close()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {majorID} not found")
        session.close()