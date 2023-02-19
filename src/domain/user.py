from sqlalchemy import Column, Integer, String, DateTime

from src.infra.database import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)
