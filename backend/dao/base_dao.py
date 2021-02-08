from backend.models.base_model import BaseModel
from backend.dao.session import Session


class BaseDao:
    def __init__(self, type_model: BaseModel) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> BaseModel:
        if isinstance(model, BaseModel):
            with Session() as session:
                session.add(model)
                session.commit()
                session.refresh(model)
                return model
        else:
            raise TypeError(f'Model must be {BaseModel}')

    def read_all(self) -> list[BaseModel]:
        with Session() as session:
            result = session.query(self.__type_model).order_by('id').all()
            return result

    def read_by_id(self, id_: int) -> BaseModel:
        if isinstance(id_, int):
            with Session() as session:
                result = session.query(
                    self.__type_model).filter_by(id=id_).first()
                return result
        else:
            raise TypeError(f'Id must be {int}')
