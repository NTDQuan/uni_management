from typing import List, ForwardRef

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship, Mapped

from database.Base import base

Teacher = ForwardRef('User')

class Role(base):
    __tablename__ = "role"

    role_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user = Mapped[List["User"]] = relationship(back_populates="Role")
    role_name: Mapped[String] = mapped_column(String(10))
