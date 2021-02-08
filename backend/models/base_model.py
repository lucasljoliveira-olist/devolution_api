from sqlalchemy.ext.declatative import declatative_base
from sqlalchemy import Column, Integer



Base = declatative_base()

class BaseModel(Base):
  __abstract__ = True
  id = Column('id', Integer, primary_key=True)
