from backend.dao.base_dao import BaseDao
from backend.models.devolution_product_order_model import DevolutionProductOrder

class DevolutionProductOrderDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(DevolutionProductOrder)