from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from backend.models import BaseModel

class OrderProductDevolution(BaseModel):
  __tablename__ = 'order_product_devolution'
  id_order_product = Column('id_order_product' ,Integer, ForeignKey('order_product.id'), nullable=False)  
  #order_product = relationship(OrderProduct)
  id_devolution =  Column('id_devolution' ,Integer, ForeignKey('devolution.id'), nullable=False)
  devolution = relationship(Devolution)
  id_devolution_status = Column('id_devolution_status', Integer, ForeignKey('devolution_status.id'), nullable=False)
  devolution_status = relationship(DevolutionStatus)

  def __init__(self, id_order_product: int, id_devolution: int, id_devolution_status: int) -> None:
    self.id_order_product = id_order_product
    self.id_devolution = id_devolution
    self.id_devolution_status = id_devolution_status
    