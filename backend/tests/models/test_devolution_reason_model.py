import sys


sys.path.append('.')

from backend.models.devolution_reason_model import DevolutionReason as Model
from backend.models.base_model import BaseModel

import pytest


class TestDevolutionReasonModel:
    @pytest.mark.parametrize('title, description', [('T'*100, 'T'*200), ('T', 'T'), ('T'*50, 'T'*100)])
    def test_model_instance(self, title, description):
        model = Model(title, description)
        assert isinstance(model, Model)
        assert isinstance(model, BaseModel)

    def test_model_title_type(self):
        title = 'test'
        model = Model(title, 'description')
        assert model.title is title

    def test_model_description_type(self):
        description = 'test'
        model = Model('title', description)
        assert model.description is description

    @pytest.mark.parametrize('title', [10, 10.5, True])
    def test_model_not_title_type(self, title):
        with pytest.raises(TypeError):
            Model(title, 'description')

    @pytest.mark.parametrize('description', [10, 10.5, True])
    def test_model_not_description_type(self, description):
        with pytest.raises(TypeError):
            Model('title', description)

    def test_model_title_empty(self):
        with pytest.raises(ValueError):
            Model('', 'description')
    
    def test_model_description_empty(self):
        with pytest.raises(ValueError):
            Model('title', '')
    
    @pytest.mark.parametrize('title', ['T'*101, 'T'*150])
    def test_model_title_len_error(self, title):
        with pytest.raises(ValueError):
            Model(title, 'description')
    
    @pytest.mark.parametrize('description', ['T'*201, 'T'*350])
    def test_model_description_len_error(self, description):
        with pytest.raises(ValueError):
            Model('title', description)
