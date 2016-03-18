#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CodeableConcept)
#  Date: 2016-03-18.


from . import element

class CodeableConcept(element.Element):
    """ Concept - reference to a terminology or just  text.

    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """

    __tablename__ = "CodeableConcept"

    coding = Column(Coding)
    """ Code defined by a terminology system.
        List of `Coding` items (represented as `dict` in JSON). """

    text = Column()
    """ Plain text representation of the concept.
        Type `str`. """

    def __init__(self, coding, text,):
        """ Initialize all valid properties.
        """
        self.coding = coding
        self.text = text

    def __repr__(self):
        return '<CodeableConcept %r>' % 'self.property'  # replace self.property


from . import coding