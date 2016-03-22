#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CodeableConcept)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class CodeableConcept(complex_dt.ComplexElement):
    """ Concept - reference to a terminology or just  text.

    A concept that may be defined by a formal reference to a
    terminology or ontology or may be provided by text.
    """

    __tablename__ = "CodeableConcept"

    coding = Column(primitives.StringField, ForeignKey('Coding.id'))
    """ Code defined by a terminology system.
        List of `Coding` items (represented as `dict` in JSON). """

    text = Column(primitives.StringField)
    """ Plain text representation of the concept.
        Type `str`. """

    def __init__(self, coding, text, ):
        """ Initialize all valid properties.
        """
        self.coding = coding
        self.text = text

    def __repr__(self):
        return '<CodeableConcept %r>' % 'self.property'  # replace self.property
