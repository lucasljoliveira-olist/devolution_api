from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, validates
from backend.models.base_model import BaseModel
from backend.models.devolution_model import Devolution
from backend.models.devolution_status_model import DevolutionStatus
from backend.utils.validators import validate_type


class DevolutionProductOrder(BaseModel):
    __tablename__ = 'devolution_product_order'
    id_order_product = Column('id_order_product', Integer, ForeignKey(
        'order_product.id'), nullable=False)
    #order_product = relationship(OrderProduct)
    id_devolution = Column('id_devolution', Integer,
                           ForeignKey('devolution.id'), nullable=False)
    devolution = relationship(Devolution)
    id_devolution_status = Column('id_devolution_status', Integer, ForeignKey(
        'devolution_status.id'), nullable=False)
    devolution_status = relationship(DevolutionStatus)

    def __init__(self, id_order_product: int, id_devolution: int, id_devolution_status: int) -> None:
        self.id_order_product = id_order_product
        self.id_devolution = id_devolution
        self.id_devolution_status = id_devolution_status

    @validates('id_order_product', 'id_devolution', 'id_devolution_status')
    def validate_id(self, key: str, id: int):
        validate_type(id, int, key)
        return id
