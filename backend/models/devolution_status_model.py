from sqlalchemy import Column, String
from backend.models import BaseModel

class DevolutionStatus(BaseModel):
  __tablename__ = 'devolution_status'
  name = Column('name' , String(length=100), nullable=False)
  description = Column('description' , String(length=200), nullable=False)


  def __init__(self, name: str, description: str) -> None:
    self.name = name
    self.description = description

