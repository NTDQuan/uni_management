from database.initSession import session
from sqlalchemy.orm import sessionmaker

from university_management.src.database.Connect import engine
from university_management.src.model.Model import Class


def delete_class(classID: int) -> None:
    Session = sessionmaker(bind=engine)
    session = Session()
    deleted_class = session.query(Class).get(classID)
    if deleted_class:
        session.delete(deleted_class)
        session.commit()
        session.close()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {classID} not found")
        session.close()