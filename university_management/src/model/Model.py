from typing import List, ForwardRef

from sqlalchemy import ForeignKey, DateTime, func, Integer, String
from sqlalchemy.orm import Mapped, declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = "role"

    role_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name: Mapped[String] = mapped_column(String(10))
    users: Mapped[List["User"]] = relationship(back_populates="role")


class User(Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student: Mapped["Student"] = relationship(back_populates="user", cascade="all, delete, delete-orphan")
    lecturer: Mapped["Lecturer"] = relationship(back_populates="user")
    hashed_pass: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"))
    role: Mapped["Role"] = relationship(back_populates="users")

class Gender(Base):
    __tablename__ = "gender"

    gender_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gender_name: Mapped[str] = mapped_column(String(6))
    students: Mapped[List["Student"]] = relationship(back_populates="gender")
    lecturers: Mapped[List["Lecturer"]] = relationship(back_populates="gender")

class Major(Base):
    __tablename__ = "major"

    major_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    major_name: Mapped[str] = mapped_column(String(50))
    students: Mapped[List["Student"]] = relationship(back_populates="major")
    lecturers: Mapped[List["Lecturer"]] = relationship(back_populates="major")
    course: Mapped["Course"] = relationship(back_populates="major")

class Student(Base):
    __tablename__ = "student"

    student_id: Mapped[int] = mapped_column(ForeignKey("user.user_id") ,primary_key=True, onupdate="CASCADE")
    user: Mapped["User"] = relationship(back_populates="student", cascade="all, delete, delete-orphan", single_parent=True)
    first_name: Mapped[str] = mapped_column(String(10))
    last_name: Mapped[str] = mapped_column(String(50))
    telephone: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column(String(60))
    credit: Mapped[int] = mapped_column(Integer)
    year: Mapped[int] = mapped_column(Integer)
    profile_image: Mapped[str] = mapped_column(String(100))
    gender_id: Mapped[int] = mapped_column(ForeignKey("gender.gender_id"))
    gender: Mapped["Gender"] = relationship(back_populates="students")
    major_id: Mapped[int] = mapped_column(ForeignKey("major.major_id"))
    major: Mapped["Major"] = relationship(back_populates="students")

class Lecturer(Base):
    __tablename__ = "lecturer"

    lecturer_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="lecturer", cascade="all, delete, delete-orphan", single_parent=True)
    first_name: Mapped[str] = mapped_column(String(10))
    last_name: Mapped[str] = mapped_column(String(50))
    telephone: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column(String(60))
    profile_image: Mapped[str] = mapped_column(String(100))
    gender_id: Mapped["Gender"] = mapped_column(ForeignKey("gender.gender_id"))
    gender: Mapped["Gender"] = relationship(back_populates="lecturers")
    major_id: Mapped["Major"] = mapped_column(ForeignKey("major.major_id"))
    major: Mapped["Major"] = relationship(back_populates="lecturers")
    class_id: Mapped[List["Class"]] = relationship(back_populates="rclass")

class Course(Base):
    __tablename__ = "course"

    course_id: Mapped[int] = mapped_column(primary_key=True)
    course_name: Mapped[str] = mapped_column(String(50))
    course_credit: Mapped[int] = mapped_column(Integer)
    major_id: Mapped[int] = mapped_column(ForeignKey("major.major_id"))
    major: Mapped["Major"] = relationship(back_populates="course")
    cclass: Mapped[List["Class"]] = relationship(back_populates="course")

class Class(Base):
    __tablename__ = "class"

    class_id: Mapped[int] = mapped_column(primary_key=-True)
    class_name: Mapped[str] = mapped_column(String(50))
    semester: Mapped[int] = mapped_column(Integer)
    year: Mapped[int] = mapped_column(Integer)
    lecturer_id: Mapped[int] = mapped_column(ForeignKey(Lecturer.lecturer_id), nullable=True)
    rclass: Mapped["Lecturer"] = relationship(back_populates="class_id")
    course_id: Mapped[int] = mapped_column(ForeignKey("course.course_id"))
    course: Mapped["Course"] = relationship(back_populates="cclass")
    status: Mapped[str] = mapped_column(String(50))
    start_period: Mapped[int] = mapped_column(Integer)
    end_period: Mapped[int] = mapped_column(Integer)
    day: Mapped[int] = mapped_column(Integer)
