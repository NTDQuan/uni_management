import hashlib

def hashPassword(password):
    """
    Return hased password (md5)
        Parameter:
            password (Str)
        Returns:
            hashed: hashed password
    """
    salt = "21522499"
    database_password = password + salt
    hashed = hashlib.md5(database_password.encode())
    return hashed.hexdigest()