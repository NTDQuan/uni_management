import hashlib
from mysql.connector import Error
from model.Model import User, Role
from database.initSession import session
from util.hashPassword import hashPassword
from util.role import role
import mysql.connector

from university_management.src.config import state


class Authentication:
    """Class handle authentication"""
    def __init__(self):
        self.__role = None
    def authentication(self, username, password):
        """
        Args:
            username(string): user name
            password(string): password

        Returns:
            int: The login state

        """
        result = session.query(User).filter(User.user_id == username).first()
        print("Login")
        if result is None:
            print("No user")
            return 0
        else:
            print("Found user")
            if hashPassword(password) == result.hashed_pass:
                print("valid user, logged in")
                self.__role = result.role
                state = "LOGGED_IN"
                print("State: " + state)
                self.__role = role(result.role_id)
                print("Role: " + self.__role)
                return 1
            else:
                print("Invalid pass")
                return 0




        
        
        

