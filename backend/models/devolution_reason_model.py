from sqlalchemy import Column, String
from backend.models import BaseModel

class DevolutionReason(BaseModel):
  __tablename__ = 'devolution_reason'
  title = Column('title' , String(length=100), nullable=False)
  description = Column('description' , String(length=200), nullable=False)
  

  def __init__(self, title: str, description: str) -> None:
    self.title = title
    self.description = description