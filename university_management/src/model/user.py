import mysql.connector
from ..database.ConnectionPoolHolder import ConnectionPoolHolder

class user:

    def __init__(self):
        mysql_pool = ConnectionPoolHolder().getConnectionPool()
        mysql_pool.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                user_name VARCHAR(50),
                hashed_password VARCHAR(40),
                email VARCHAR(50),
                role_id INTEGER,
                created_at DATETIME,
                modified_date DATETIME
            )
            """
        )

if __name__ == "__main__":
    u = user()