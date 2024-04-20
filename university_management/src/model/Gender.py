from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from database.Base import base


class Gender(base):
    __tablename__ = "Gender"

    gender_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    gender_name: Mapped[str] = mapped_column(String(6))