from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.infra.database import Base


class Gecko(Base):
    __tablename__ = "gecko"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User")
    create_date = Column(DateTime, nullable=False)
