from backend.dao.base_dao import BaseDao
from backend.models.devolution_model import Devolution

class DevolutionDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Devolution)