from flask_restful import marshal_with, fields
from backend.dao.devolution_product_order_dao import DevolutionProductOrderDao as Dao
from backend.models.devolution_product_order_model import DevolutionProductOrder as Model
from backend.resources.base_resource import BaseResource

class DevolutionProductOrderResource(BaseResource):
  fields = {
    'id': fields.Integer,
    'id_order_product': fields.Integer,
    'id_devolution': fields.Integer,
    'id_devolution_status': fields.Integer
  }

  def __init__(self):
    self.__dao = Dao()
    self.__model_type = Model
    super().__init__(self.__dao, self.__model_type)
  
  @marshal_with(fields)
  def get(self, id_: int):
    return super().get(id_)
  
  @marshal_with(fields)
  def post(self):
    return super().post()
  
  @marshal_with(fields)
  def put(self, id_: int):
    return super().put(id_)