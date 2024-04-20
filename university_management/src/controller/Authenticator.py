import hashlib
from .config import DBCONFIG
from mysql.connector import Error
import mysql.connector


class Authentication:
    def __init__(self):
        pass

    def authentication(username, password):
        pass

if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    authen = Authentication()
    authen.authenticate(username, password)
        
        
        

