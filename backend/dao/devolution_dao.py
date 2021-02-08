from backend.dao.base_dao import BaseDao
from backend.models.devolution_model import DevolutionModel

class DevolutionDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(DevolutionModel)