from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    company_size = Column(String)
    job_title = Column(String)
    website = Column(String)
    message = Column(String)
    score = Column(String)
