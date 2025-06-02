# utils/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

# Initialize the session maker
Session = None

def init_db():
    """Initialize the database and create tables"""
    global Session
    engine = create_engine('sqlite:///subtrackr.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session