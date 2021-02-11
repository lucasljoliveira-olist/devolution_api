import sys


sys.path.append('.')

from backend.models.devolution_product_order_model import DevolutionProductOrder as Model
from backend.models.base_model import BaseModel

import pytest


class TestDevolutionProductOrderModel:
    @pytest.mark.parametrize('''id_order_product, id_devolution, 
        id_devolution_status''',
        [(1, 2, 3), 
         (10, 20, 30), 
         (100, 200, 300)])
    def test_model_instance(self, id_order_product, id_devolution, 
        id_devolution_status):
        model = Model(id_order_product, id_devolution, 
            id_devolution_status)
        assert isinstance(model, Model)
        assert isinstance(model, BaseModel)


    @pytest.mark.parametrize('''id_order_product, id_devolution, 
        id_devolution_status''',
        [('1', 1, 1), 
         (1, '1', 1),
         (1, 1, '1')])
    def test_model_not_id_order_type(self, id_order_product, id_devolution, 
        id_devolution_status):
        with pytest.raises(TypeError):
            model = Model(id_order_product, id_devolution, 
                id_devolution_status)
