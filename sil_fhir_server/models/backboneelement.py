#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/BackboneElement)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import element

class BackboneElement(element.Element):
    """ Base for elements defined inside a resource.

    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """

    __tablename__ = "BackboneElement"
    
    modifierExtension = Column(Extension)
    """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """

    def __init__(self, modifierExtension,):
        """ Initialize all valid properties.
        """
        self.modifierExtension = modifierExtension

    def __repr__(self):
        return '<BackboneElement %r>' % 'self.property'  # replace self.property


from . import extension