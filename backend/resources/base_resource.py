from flask_restful import Resource
from flask import request
from backend.dao.base_dao import BaseDao
from backend.models.base_model import BaseModel

class BaseResource(Resource):
  def __init__(self, dao: BaseDao, model_type: BaseModel):
    self.__dao = dao
    self.__model_type = model_type

  def get(self, id_: int=None):
    if id_:
      return self.__dao.read_by_id(id_), 200
    return self.__dao.read_all(), 200
  
  def post(self):
    data = request.json
    item = self.__model_type(**data)
    return self.__dao.save(item), 201
  
  def put(self, id_: int):
    data = request.json
    if data['id_'] == id_:
      item = self.__dao.read_by_id(id_)
      for key, value in data.items():
        setattr(item, key, value)
      return self.__dao.save(item), 201
    return None, 404
  
  def delete(self, id_: int):
    item = self.__dao.read_by_id(id_)
    self.__dao.delete(item)
    return None, 204