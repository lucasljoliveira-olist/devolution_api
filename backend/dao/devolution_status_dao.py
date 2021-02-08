from backend.dao.base_dao import BaseDao
from backend.models.devolution_status_model import DevolutionStatus

class DevolutionStatusDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(DevolutionStatus)