from sqlalchemy import Column, Integer, String, Text
from .db import Base

class IntakeRecord(Base):
    __tablename__ = "intake_records"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    business_type = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    urgency = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
