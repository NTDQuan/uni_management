from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from database.Base import base

class Major(base):
    __tablename__ = "major"

    major_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    major_name: Mapped[str] = mapped_column(String(50))