from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from .Connect import engine
from model.Model import Base

print("CREATING TABLES >>>> ")

def create_all_table():
    try:
        with engine.connect() as connection:
            result = connection.execute(text('select "Hello"'))
            print(result.all())

        Base.metadata.create_all(bind=engine, checkfirst=True)
        print("Table created successfully")
    except Exception as e:
        print("Error creating tables:", e)

def getSession():
    Session = sessionmaker(bind = engine)
    session = Session()
    return session