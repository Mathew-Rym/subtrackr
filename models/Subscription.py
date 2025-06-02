from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    billing_cycle = Column(String, nullable=False)  # 'monthly', 'yearly', 'weekly'
    next_payment_date = Column(Date, nullable=False)
    
    user = relationship("User", back_populates="subscriptions")
    reminders = relationship("Reminder", back_populates="subscription")