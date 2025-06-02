from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    subscriptions = relationship("Subscription", backref="user")

class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

engine = create_engine('sqlite:///subtrackr.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add test data
user = User(username="testuser")
session.add(user)
session.commit()

sub = Subscription(name="Netflix", cost=15.99, user_id=user.id)
session.add(sub)
session.commit()

print("SUCCESS! Database created with:")
print("- Users:", session.query(User).count())
print("- Subs:", session.query(Subscription).count())
