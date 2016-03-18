#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Annotation)
#  Date: 2016-03-18.


from . import element

class Annotation(element.Element):
    """ Text node with attribution.

    A  text note which also  contains information about who made the statement
    and when.
    """

    __tablename__ = "Annotation"

    authorReference = Column()
    """ Individual responsible for the annotation.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """

    authorString = Column()
    """ Individual responsible for the annotation.
        Type `str`. """

    text = Column()
    """ The annotation  - text content.
        Type `str`. """

    time = Column()
    """ When the annotation was made.
        Type `FHIRDate` (represented as `str` in JSON). """

    def __init__(self, authorReference, authorString, text, time,):
        """ Initialize all valid properties.
        """
        self.authorReference = authorReference
        self.authorString = authorString
        self.text = text
        self.time = time

    def __repr__(self):
        return '<Annotation %r>' % 'self.property'  # replace self.property


from . import fhirdate
from . import fhirreference