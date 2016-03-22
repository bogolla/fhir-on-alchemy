#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Ratio)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Ratio(complex_dt.ComplexElement):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    __tablename__ = "Ratio"
    
    denominator = Column(primitives.StringField,
                         ForeignKey('Quantity.id'))
    """ Denominator value.
        Type `Quantity` (represented as `dict` in JSON). """
    
    numerator = Column(primitives.StringField,
                       ForeignKey('Quantity.id'))
    """ Numerator value.
        Type `Quantity` (represented as `dict` in JSON). """

    def __init__(self, denominator, numerator):
        """ Initialize all valid properties.
        """
        self.denominator = denominator
        self.numerator = numerator

    def __repr__(self):
        return '<Ratio %r/%r>' % (self.numerator, self.denominator)
