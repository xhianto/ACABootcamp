from datetime import datetime
from ..app import db_base
from sqlalchemy import Column, String, Integer, Date, DateTime

class People(db_base):

    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(1), nullable=False)
    email = Column(String(500), nullable=False)
    dob = Column(Date, nullable=False)
    likes = Column(Integer, default=0, nullable=False)
    dislikes = Column(Integer, default=0, nullable=False)
    inserted = Column(DateTime, default=datetime.now)
    last_updated = Column(DateTime, onupdate=datetime.now)

    def __init__(self, first_name=None, last_name=None, gender=None, email=None, dob=None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.dob = dob
