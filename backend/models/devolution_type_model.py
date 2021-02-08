from sqlalchemy import Column, String
from backend.models import BaseModel

class DevolutionType(BaseModel):
  __tablename__ = 'devolution_type'
  name = Column('name' , String(length=100), nullable=False)
  description = Column('description' , String(length=200), nullable=False)

  def __init__(self, name: str, description: str) -> None:
    self.name = name
    self.description = description