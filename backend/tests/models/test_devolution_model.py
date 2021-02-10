import pytest
from backend.models.devolution_model import Devolution as Model
from backend.models.base_model import BaseModel
from datetime import datetime
import sys
sys.path.append('.')


class TestDevolutionModel:
    def test_devolution_instance(self):
        devolution = Model(1, 2, 3, datetime, 'br' )
        assert isinstance(devolution, Model)
        assert isinstance(devolution, BaseModel)

    @pytest.mark.parametrize('id_order', [1])
    def test_devolution_id_is_int(self, id):
        devolution = Model(id_order, 5)
        assert isinstance(devolution.name, str)

    @pytest.mark.parametrize('description', ['Teste', 'T'*255, 'T', ''])
    def test_devolution_description_type(self, description):
        devolution = Model('Name', description, 10.50, 5)
        assert isinstance(devolution.description, str)

    @pytest.mark.parametrize('price', [1.0, 100.0, 10.5])
    def test_devolution_price_type(self, price):
        devolution = Model('Name', 'Desc', price, 5)
        assert isinstance(devolution.price, float)

    @pytest.mark.parametrize('amount', [0, 100, 10])
    def test_devolution_amount_type(self, amount):
        devolution = Model('Name', 'Desc', 10.50, amount)
        assert isinstance(devolution.amount, int)

    @pytest.mark.parametrize('name', [1, True, 10.5])
    def test_devolution_name_type_error(self, name):
        with pytest.raises(TypeError):
            devolution = Model(name, 'Desc', 10.50, 5)

    @pytest.mark.parametrize('description', [1, True, 10.5])
    def test_devolution_description_type_error(self, description):
        with pytest.raises(TypeError):
            devolution = Model('Name', description, 10.50, 5)

    @pytest.mark.parametrize('price', ['', 10])
    def test_devolution_price_type_error(self, price):
        with pytest.raises(TypeError):
            devolution = Model('Name', 'Desc', price, 5)

    @pytest.mark.parametrize('amount', ['', [], 10.5])
    def test_devolution_amount_type_error(self, amount):
        with pytest.raises(TypeError):
            devolution = Model('Name', 'Desc', 10.5, amount)

    def test_devolution_name_len_error(self):
        with pytest.raises(ValueError):
            devolution = Model('T'*101, '', 10.5, 10)

    def test_devolution_name_empty_error(self):
        with pytest.raises(ValueError):
            devolution = Model('', '', 10.5, 10)

    def test_devolution_description_len_error(self):
        with pytest.raises(ValueError):
            devolution = Model('Name', 'T'*256, 10.5, 10)

    @pytest.mark.parametrize('price', [0.0, -1.0, -100.0])
    def test_devolution_price_greatter_than_error(self, price):
        with pytest.raises(ValueError):
            devolution = Model('Name', 'Desc', price, 10)

    @pytest.mark.parametrize('amount', [-1, -10, -100])
    def test_devolution_price_greatter_than_error(self, amount):
        with pytest.raises(ValueError):
            devolution = Model('Name', 'Desc', 10.0, amount)
