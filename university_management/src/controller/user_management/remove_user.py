from database.initSession import session
from model.Model import User

def deleteUser(userID: int) -> None:
    user = session.query(User).get(userID)
    print(user)
    if user:
        session.delete(user)
        session.commit()
    else:
        # Handle user not found scenario (optional)
        print(f"User with ID {userID} not found")