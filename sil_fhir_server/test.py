from .models_mock import Result
from sqlalchemy import Column, String


class Test(Result):
    __tablename__ = 'ya_pili'
    uhhrl = Column(String)