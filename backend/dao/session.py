from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    session = sessionmaker(self.__engine)
    self.__session = session()
    return self.__session
  
  def __exit__(self, type, value, traceback):
    self.__session.close()
    self.__engine.dispose()
