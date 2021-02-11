import sys


sys.path.append('.')

from backend.models.devolution_model import Devolution as Model
from backend.models.base_model import BaseModel

import pytest


class TestDevolutionModel:
    @pytest.mark.parametrize('''id_order, id_devolution_type, 
        id_devolution_reason, id_devolution_status, buyer_reason''',
        [(1, 2, 3, 4, 'T'), 
         (10, 20, 30, 40, 'T'*150), 
         (100, 200, 300, 400, 'T'*300)])
    def test_model_instance(self, id_order, id_devolution_type, 
        id_devolution_reason, id_devolution_status, buyer_reason):
        model = Model(id_order, id_devolution_type, 
            id_devolution_reason, id_devolution_status, buyer_reason)
        assert isinstance(model, Model)
        assert isinstance(model, BaseModel)


    @pytest.mark.parametrize('''id_order, id_devolution_type, 
        id_devolution_reason, id_devolution_status, buyer_reason''',
        [('1', 1, 1, 1, 'T'), 
         (1, '1', 1, 1, 'T'*150),
         (1, 1, '1', 1, 'T'*200),
         (1, 1, 1, '1', 'T'*300)])
    def test_model_not_id_order_type(self, id_order, id_devolution_type, 
        id_devolution_reason, id_devolution_status, buyer_reason):
        with pytest.raises(TypeError):
            model = Model(id_order, id_devolution_type, 
                id_devolution_reason, id_devolution_status, buyer_reason)


    def test_model_buyer_reason_type(self):
        buyer_reason = 'test'
        model = Model(1, 1, 1, 1, buyer_reason)
        assert model.buyer_reason is buyer_reason


    @pytest.mark.parametrize('buyer_reason', [10, 10.5, True])
    def test_model_not_buyer_reason_type(self, buyer_reason):
        with pytest.raises(TypeError):
            Model(1, 1, 1, 1, buyer_reason)


    def test_model_buyer_reason_empty(self):
        with pytest.raises(ValueError):
            Model(1, 1, 1, 1, '')
    
    
    @pytest.mark.parametrize('buyer_reason', ['T'*301, 'T'*350])
    def test_model_buyer_reason_len_error(self, buyer_reason):
        with pytest.raises(ValueError):
            Model(1, 1, 1, 1, buyer_reason)
