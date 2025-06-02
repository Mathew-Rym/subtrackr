from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Reminder(Base):
    __tablename__ = 'reminders'
    
    id = Column(Integer, primary_key=True)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    reminder_date = Column(Date, nullable=False)
    message = Column(String)
    
    subscription = relationship("Subscription", back_populates="reminders")