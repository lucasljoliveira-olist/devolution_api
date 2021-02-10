from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models.base_model import BaseModel

class Session:
  def __init__(self):
    connector = 'postgresql'
    host = 'pgsql08-farm15.uni5.net'
    database = 'topskills14'
    user = 'topskills14'
    password = 'olist21'
    port = '5432'
    self.__connection_string = f'{connector}://{user}:{password}@{host}:{port}/{database}'
  
  def __enter__(self):
    self.__engine = create_engine(self.__connection_string)
    self.__create_tables()
    session = sessionmaker(self.__engine)
    self.__session = session()
    return self.__session
  
  def __exit__(self, type, value, traceback):
    self.__session.close()
    self.__engine.dispose()
  
  def __create_tables(self):
    BaseModel.metadata.bind = self.__engine
    BaseModel.metadata.create_all()
