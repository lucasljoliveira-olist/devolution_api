import sys


sys.path.append('.')

from backend.models.devolution_type_model import DevolutionType as Model
from backend.models.base_model import BaseModel

import pytest


class TestDevolutionTypeModel:
    @pytest.mark.parametrize('name, description', [('T'*100, 'T'*200), ('T', 'T'), ('T'*50, 'T'*100)])
    def test_model_instance(self, name, description):
        model = Model(name, description)
        assert isinstance(model, Model)
        assert isinstance(model, BaseModel)

    def test_model_name_type(self):
        name = 'test'
        model = Model(name, 'description')
        assert model.name is name

    def test_model_description_type(self):
        description = 'test'
        model = Model('name', description)
        assert model.description is description

    @pytest.mark.parametrize('name', [10, 10.5, True])
    def test_model_not_name_type(self, name):
        with pytest.raises(TypeError):
            Model(name, 'description')

    @pytest.mark.parametrize('description', [10, 10.5, True])
    def test_model_not_description_type(self, description):
        with pytest.raises(TypeError):
            Model('name', description)

    def test_model_name_empty(self):
        with pytest.raises(ValueError):
            Model('', 'description')
    
    def test_model_description_empty(self):
        with pytest.raises(ValueError):
            Model('name', '')
    
    @pytest.mark.parametrize('name', ['T'*101, 'T'*150])
    def test_model_name_len_error(self, name):
        with pytest.raises(ValueError):
            Model(name, 'description')
    
    @pytest.mark.parametrize('description', ['T'*201, 'T'*350])
    def test_model_description_len_error(self, description):
        with pytest.raises(ValueError):
            Model('name', description)
