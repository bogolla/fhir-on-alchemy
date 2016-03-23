#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/BackboneElement)
#  Date: 2016-03-22.


from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declared_attr

from sil_fhir_server.data_types import primitives
from . import element


class BackboneElement(element.Element):
    """ Base for elements defined inside a resource.

    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """

    __tablename__ = "BackboneElement"
    __abstract__ = True

    @declared_attr
    def modifierExtension(cls):
        return Column(primitives.StringField, ForeignKey('Extension.id'))
    # modifierExtension = Column(primitives.StringField,
    #                            ForeignKey('Extension.id'))
    """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """

    def __init__(self, modifierExtension):
        """ Initialize all valid properties.
        """
        self.modifierExtension = modifierExtension

    def __repr__(self):
        return '<BackboneElement %r>' % 'self.property'  # replace self.property
