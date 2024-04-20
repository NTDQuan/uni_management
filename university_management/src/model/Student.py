from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.Base import base
from university_management.src.model import User


class Student(base):
    __tablename__ = "student"

    teacher_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(10))
    last_name: Mapped[str] = mapped_column(String(50))
    telephone: Mapped[str] = mapped_column(String(11))
    address: Mapped[str] = mapped_column(String(60))
    profile_image: Mapped[str] = mapped_column(String(100))
    major_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped["User"] = mapped_column(ForeignKey("user.user_id"))
    user: Mapped["User"] = relationship(back_populates = 'comments')

