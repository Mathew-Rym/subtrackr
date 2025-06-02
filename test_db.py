from sqlalchemy import create_engine
from models import Base

engine = create_engine('sqlite:///subtrackr.db')
Base.metadata.create_all(engine)
print("Success! Created tables:", Base.metadata.tables.keys())
