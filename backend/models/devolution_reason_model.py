from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from backend.models.base_model import BaseModel
from backend.utils.validators import validate_string_not_empty, validate_type, validate_length


class DevolutionReason(BaseModel):
    __tablename__ = 'devolution_reason'
    title = Column('title', String(length=100), nullable=False)
    description = Column('description', String(length=200), nullable=False)

    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
    

    @validates('title')
    def validate_title(self, key: str, title: str):
        validate_type(title, str, key)
        validate_string_not_empty(title, key)
        validate_length(title, 100, key)
        return title
    
    @validates('description')
    def validate_description(self, key: str, description: str):
        validate_type(description, str, key)
        validate_string_not_empty(description, key)
        validate_length(description, 200, key)
        return description
