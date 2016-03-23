#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Element)
#  Date: 2016-03-22.


from sqlalchemy import Column

from app import db
from sil_fhir_server.data_types import primitives


# todo class Element(fhirabstractbase.FHIRAbstractBase):
class Element(db.Model):
    """ Base for all elements.

    Base definition for all elements in a resource.
    """

    __tablename__ = "Element"
    __abstract__ = True
    __mapper_args__ = {'always_refresh': True}
    
    # todo extension = Column(primitives.StringField, ForeignKey('Extension.id'))
    """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
    
    id = Column(primitives.StringField, primary_key=True)
    """ xml:id (or equivalent in JSON).
        Type `str`. """

    def __init__(self, extension, id,):
        """ Initialize all valid properties.
        """
        self.extension = extension
        self.id = id

    def __repr__(self):
        return '<Element %r>' % 'self.property'  # replace self.property