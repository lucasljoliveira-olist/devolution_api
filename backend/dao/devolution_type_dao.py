from backend.dao.base_dao import BaseDao
from backend.models.devolution_type_model import DevolutionType

class DevolutionTypeDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(DevolutionType)