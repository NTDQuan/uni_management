from sqlalchemy import create_engine

"""
database connection string and engine
"""
connection_string = "mysql+pymysql://root:quanhtht123@127.0.0.1:3306/uni_management"
engine = create_engine(connection_string, echo=True)