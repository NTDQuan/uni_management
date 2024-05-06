from university_management.src.database.initSession import session
from university_management.src.model.Model import Major


def delete_major(majorID: int) -> None:
    major = session.query(Major).get(majorID)
    print(major)
    if major:
        session.delete(major)
        session.commit()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {majorID} not found")