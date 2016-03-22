#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Identifier)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Identifier(complex_dt.ComplexElement):
    """ An identifier intended for computation.

    A technical identifier - identifies some entity uniquely and unambiguously.
    """

    __tablename__ = "Identifier"

    # TODO
    # assigner = Column(primitives.StringField,
    #                   ForeignKey('FHIRReference.id'))
    """ Organization that issued id (may be just text).
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """

    period = Column(primitives.StringField,
                    ForeignKey('Period.id'))
    """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """

    system = Column(primitives.StringField)
    """ The namespace for the identifier.
        Type `str`. """

    type = Column(primitives.StringField,
                  ForeignKey('CodeableConcept.id'))
    """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    use = Column(primitives.StringField)
    """ usual | official | temp | secondary (If known).
        Type `str`. """

    value = Column(primitives.StringField)
    """ The value that is unique.
        Type `str`. """

    def __init__(self, assigner, period, system, type, use, value):
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
