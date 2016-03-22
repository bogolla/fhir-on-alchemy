#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Annotation)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Annotation(complex_dt.ComplexElement):
    """ Text node with attribution.

    A  text note which also  contains information about who made the
    statement and when.
    """

    __tablename__ = "Annotation"

    # TODO
    # authorReference = Column(primitives.StringField,
    #                          ForeignKey('FHIRReference.id'))
    """ Individual responsible for the annotation.
        Type `FHIRReference` referencing `Practitioner, Patient,
        RelatedPerson` (represented as `dict` in JSON). """

    authorString = Column(primitives.StringField)
    """ Individual responsible for the annotation.
        Type `str`. """

    text = Column(primitives.StringField)
    """ The annotation  - text content.
        Type `str`. """

    time = Column(primitives.DateTimeField)
    """ When the annotation was made.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, authorReference, authorString, text, time):
        """ Initialize all valid properties.
        """
        self.authorReference = authorReference
        self.authorString = authorString
        self.text = text
        self.time = time

    def __repr__(self):
        return '<Annotation %r>' % 'self.property'  # replace self.property
