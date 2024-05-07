from model.Model import User, Lecturer, Student
from util.hashPassword import hashPassword
from database.initSession import session
from abc import ABC, abstractmethod

def add_user(user_data: dict):
    user = User(user_id = user_data["User_id"], hashed_pass = hashPassword(user_data["Password"]), email = user_data["User_email"], role_id = user_data["User_role"])
    session.add(user)

def add_lecturer(lecturer_data: dict):
    lecturer = Lecturer(lecture_id = lecturer_data["Lecturer_id"], first_name = lecturer_data["firstName"], last_name = lecturer_data["lastName"], telephone = lecturer_data["telephone"], address = lecturer_data["address"], profile_image = lecturer_data["profile_image"], gender_id = lecturer_data["gender"], major_id = lecturer_data["major"])
    session.add(lecturer)

def add_student(student_data: dict):
    student = Student(student_id = student_data["Student_id"], first_name = student_data["firstName"], last_name = student_data["lastName"], telephone = student_data["telephone"], address = student_data["address"], profile_image = student_data["profile_image"], gender_id = student_data["gender"], major_id = student_data["major"], credit = student_data["credit"], year = student_data["year"])
    session.add(student)

class UserFactory:
    @classmethod
    def create_user(cls, user_data: dict, profile_data: dict):
        add_user(user_data)
        if user_data["User_role"] == 2:
            add_lecturer(profile_data)
        elif user_data["User_role"] == 3:
            print("Creating student")
            add_student(profile_data)
        session.commit()
