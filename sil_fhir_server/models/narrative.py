#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Narrative)
#  Date: 2016-03-22.


from sqlalchemy import Column
from sil_fhir_server.data_types import primitives
from . import element

class Narrative(element.Element):
    """ A human-readable formatted text, including images.
    """

    __tablename__ = "Narrative"
    
    div = Column(primitives.StringField)
    """ Limited xhtml content.
        Type `str`. """
    
    status = Column(primitives.StringField)
    """ generated | extensions | additional | empty.
        Type `str`. """

    def __init__(self, div, status,):
        """ Initialize all valid properties.
        """
        self.div = div
        self.status = status

    def __repr__(self):
        return '<Narrative %r>' % 'self.property'  # replace self.property