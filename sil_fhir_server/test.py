from collections import OrderedDict

from sqlalchemy import Column
from app import db
from sil_fhir_server.utilities.pg_composite import CompositeType
# from sqlalchemy_utils import CompositeType, CompositeArray
from sil_fhir_server.data_types import primitives


class TestType(object):
    def __init__(self):
        pass

    def test_type(self):
        self.new_type = CompositeType(
            'besha_type',
            [
                Column('name', primitives.StringField, nullable=False),
                Column('amount', primitives.IntegerField, nullable=False),
                Column('smthn', primitives.StringField)
            ]
        )
        return self.new_type


class Account(db.Model):
    __tablename__ = 'account'


    id = Column(primitives.IntegerField, primary_key=True)
    balance = Column(
        CompositeType(
            'money_type',
            [
                Column('name', primitives.StringField),
                Column('amount', primitives.IntegerField),
                Column('smthn', primitives.StringField)
            ]
        )
    )


class AccountToTest(db.Model):
    __tablename__ = 'besha_account'
    id = Column(primitives.IntegerField, primary_key=True)
    balance = Column(TestType().test_type(), nullable=False)
