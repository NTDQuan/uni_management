from database.initSession import session

from university_management.src.model.Model import Class


def delete_class(className: int) -> None:
    deleted_class = session.query(Class).filter_by(class_name = className).first()
    print(deleted_class)
    if deleted_class:
        session.delete(deleted_class)
        session.commit()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {className} not found")