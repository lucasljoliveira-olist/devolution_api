from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql.schema import ForeignKey
from backend.models.base_model import BaseModel
from datetime import datetime
from backend.utils.validators import validate_string_not_empty, validate_type, validate_length
from backend.models.devolution_type_model import DevolutionType
from backend.models.devolution_reason_model import DevolutionReason
from backend.models.devolution_status_model import DevolutionStatus


class Devolution(BaseModel):
    __tablename__ = 'devolution'
    id_order = Column('id_order', Integer, nullable=False)
    id_devolution_type = Column('id_devolution_type', Integer, ForeignKey(
        'devolution_type.id'), nullable=False)
    devolution_type = relationship(DevolutionType)
    id_devolution_reason = Column('id_devolution_reason', Integer, ForeignKey(
        'devolution_reason.id'), nullable=False)
    devolution_reason = relationship(DevolutionReason)
    id_devolution_status = Column('id_devolution_status', Integer, ForeignKey(
        'devolution_status.id'), nullable=False)
    devolution_status = relationship(DevolutionStatus)
    date = Column('date', DateTime, nullable=False)
    buyer_reason = Column('buyer_reason', String(length=300), nullable=False)

    def __init__(self, id_order: int, id_devolution_type: int,
                 id_devolution_reason: int, id_devolution_status: int,
                 buyer_reason: str) -> None:
        self.id_order = id_order
        self.id_devolution_type = id_devolution_type
        self.id_devolution_reason = id_devolution_reason
        self.id_devolution_status = id_devolution_status
        self.date = datetime.today()
        self.buyer_reason = buyer_reason

    @validates('id_order', 'id_devolution_type', 'id_devolution_reason', 'id_devolution_status')
    def validate_id(self, key: str, id: int):
        validate_type(id, int, key)
        return id

    @validates('date')
    def validate_date(self, key: str, date: datetime):
        validate_type(date, datetime, key)
        return date

    @validates('buyer_reason')
    def validate_buyer_reason(self, key: str, buyer_reason: str):
        validate_type(buyer_reason, str, key)
        validate_string_not_empty(buyer_reason, key)
        validate_length(buyer_reason, 300, key)
        return buyer_reason
