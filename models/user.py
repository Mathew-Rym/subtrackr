from sqlalchemy import Column, Integer, String
from models.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    
    subscriptions = relationship("Subscription", back_populates="user")