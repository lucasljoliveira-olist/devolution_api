from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from backend.models import BaseModel
from datetime import datetime

class Devolution(BaseModel):
    __tablename__ = 'devolution'
    id_order = Column('id_order' ,Integer, ForeignKey('order.id'), nullable=False)  
    #order = relationship(Order)
    id_devolution_type =  Column('id_devolution_type' ,Integer, ForeignKey('devolution_type.id'), nullable=False)
    devolution_type = relationship(DevolutionType)
    id_devolution_reason = Column('id_devolution_reason' ,Integer, ForeignKey('devolution_reason.id'), nullable=False)
    devolution_reason = relationship(DevolutionReason)
    id_devolution_status = Column('id_devolution_status', Integer, ForeignKey('devolution_status.id'), nullable=False)
    devolution_status = relationship(DevolutionStatus)
    date = Column('date', DateTime, nullable=False)
    buyer_reason = Column('buyer_reason' , String(length=300), nullable=False)

    def __init__(self, id_order: int, id_devolution_type: int,
        id_devolution_reason: int, id_devolution_status: int,
        date: datetime, buyer_reason: str) -> None:
        self.id_order = id_order
        self.id_devolution_type = id_devolution_type
        self.id_devolution_reason = id_devolution_reason
        self.id_devolution_status = id_devolution_status
        self.date = date
        self.buyer_reason = buyer_reason

