from backend.dao.base_dao import BaseDao
from backend.models.devolution_reason_model import DevolutionReason

class DevolutionReasonDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(DevolutionReason)