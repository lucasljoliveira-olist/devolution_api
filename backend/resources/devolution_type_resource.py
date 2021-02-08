from flask_restful import marshal_with, fields
from backend.dao.devolution_type_dao import DevolutionTypeDao as Dao
from backend.models.devolution_type_model import DevolutionType as Model
from backend.resources.base_resource import BaseResource

class DevolutionTypeResource(BaseResource):
  fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String    
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