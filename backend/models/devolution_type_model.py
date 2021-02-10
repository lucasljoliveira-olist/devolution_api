from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from backend.models.base_model import BaseModel
from backend.utils.validators import validate_string_not_empty, validate_type, validate_length


class DevolutionType(BaseModel):
    __tablename__ = 'devolution_type'
    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=200), nullable=False)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key: str, name: str):
        validate_type(name, str, key)
        validate_string_not_empty(name, key)
        validate_length(name, 100, key)
        return name
    
    @validates('description')
    def validate_description(self, key: str, description: str):
        validate_type(description, str, key)
        validate_string_not_empty(description, key)
        validate_length(description, 200, key)
        return description