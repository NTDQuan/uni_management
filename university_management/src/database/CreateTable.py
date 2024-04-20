from sqlalchemy import text

from .Connect import engine
from Base import base

print("CREATING TABLES >>>> ")

def create_all_table():
    try:
        with engine.connect() as connection:
            result = connection.execute(text('select "Hello"'))
            print(result.all())
        base.metadata.create_all(bind=engine, checkfirst=True)
        print("Table created successfully")
    except Exception as e:
        print("Error creating tables:", e)