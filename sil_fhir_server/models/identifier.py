#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Identifier)
#  Date: 2016-03-18.


from . import element

class Identifier(element.Element):
    """ An identifier intended for computation.

    A technical identifier - identifies some entity uniquely and unambiguously.
    """

    __tablename__ = "Identifier"

    assigner = Column()
    """ Organization that issued id (may be just text).
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    period = Column()
    """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """

    system = Column()
    """ The namespace for the identifier.
        Type `str`. """

    type = Column()
    """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    use = Column()
    """ usual | official | temp | secondary (If known).
        Type `str`. """

    value = Column()
    """ The value that is unique.
        Type `str`. """

    def __init__(self, assigner, period, system, type, use, value,):
        """ Initialize all valid properties.
        """
        self.assigner = assigner
        self.period = period
        self.system = system
        self.type = type
        self.use = use
        self.value = value

    def __repr__(self):
        return '<Identifier %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirreference
from . import period