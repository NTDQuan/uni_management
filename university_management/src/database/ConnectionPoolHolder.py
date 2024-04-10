from .DBConnectionPool import MySQLPooling

class ConnectionPoolHolder:
    def __init__(self):
        self.connectionPool = MySQLPooling()
    
    def getConnectionPool(self):
        return self.connectionPool