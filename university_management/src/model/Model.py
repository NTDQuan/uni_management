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
    hashed_pass: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"))
    role: Mapped["Role"] = relationship(back_populates="users")



"""
class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(10))
    last_name: Mapped[str] = mapped_column(String(50))
    telephone: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column(String(60))
    profile_image: Mapped[str] = mapped_column(String(100))
    gender: Mapped["Gender"] = mapped_column(ForeignKey("gender.gender_id"))
    major_id: Mapped["Major"] = mapped_column(ForeignKey("major.major_id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))


class Student(Base):
    __tablename__ = "student"

    teacher_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(10))
    last_name: Mapped[str] = mapped_column(String(50))
    telephone: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column(String(60))
    profile_image: Mapped[str] = mapped_column(String(100))
    gender: Mapped["Gender"] = mapped_column(ForeignKey("gender.gender_id"))
    major: Mapped["Major"] = mapped_column(ForeignKey("major.major_id"))
    user_id: Mapped["User"] = mapped_column(ForeignKey("user.user_id"))

class Role(Base):
    __tablename__ = "role"

    role_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_name: Mapped[String] = mapped_column(String(10))

class Major(Base):
    __tablename__ = "major"

    major_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    major_name: Mapped[str] = mapped_column(String(50))

class Gender(Base):
    __tablename__ = "gender"

    gender_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gender_name: Mapped[str] = mapped_column(String(6))
    
"""