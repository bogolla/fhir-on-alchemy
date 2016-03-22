from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declared_attr

from sil_fhir_server.data_types import primitives
from app import db

# from sil_fhir_server.models import (
#     extension
# )


class ComplexElement(db.Model):
    """ Base for all complex elements.

    Base definition for all complex elements in a resource.
    """

    def __tablename__(cls):
        return cls.__name__

    __abstract__ = True
    __mapper_args__ = {'always_refresh': True}

    # extension = Column(primitives.StringField,
    #                    ForeignKey('Extension.id'))
    """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """

    id = Column(primitives.StringField, primary_key=True)
    """ xml:id (or equivalent in JSON).
        Type `str`. """

    def __init__(self, extension, id,):
        """ Initialize all valid properties. """
        self.extension = extension
        self.id = id

    def __repr__(self):
        # return '<Element %r>' % 'self.extension'
        pass
