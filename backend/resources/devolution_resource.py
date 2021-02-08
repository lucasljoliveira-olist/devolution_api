from flask_restful import marshal_with, fields
from backend.dao.devolution_dao import DevolutionDao
from backend.models.devolution_model import Devolution
from backend.resources.base_resource import BaseResource

class DevolutionResource(BaseResource):
  fields = {
    'id': fields.Integer,
    'id_order': fields.Integer,
    'id_devolution_type': fields.Integer,
    'id_devolution_reason': fields.Integer, 
    'id_devolution_status': fields.Integer,
    'data': fields.DateTime,
    'buyer_reason': fields.String
  }

  def __init__(self):
    self.__dao = DevolutionDao()
    self.__model_type = Devolution
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
