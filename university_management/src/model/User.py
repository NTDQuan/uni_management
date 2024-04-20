from typing import List, ForwardRef

from sqlalchemy import ForeignKey, DateTime, func, Integer, String
# from database.Base import base
from sqlalchemy.orm import Mapped, declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from database.Base import base

Student = ForwardRef('Student')
Teacher = ForwardRef('Teacher')

class User(base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    hashed_pass: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"))
    role = relationship("Role", back_populates="user")
    students: Mapped[List["Student"]] = relationship(back_populates='user')
    teachers: Mapped[List["Teacher"]] = relationship(back_populates='user')
