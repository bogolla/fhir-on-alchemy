#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Range)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives
from . import complex_dt


class Range(complex_dt.ComplexElement):
    """ Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """

    __tablename__ = "Range"

    high = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ High limit.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    low = Column(primitives.StringField, ForeignKey('Quantity.id'))
    """ Low limit.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    def __init__(self, high, low):
        """ Initialize all valid properties.
        """
        self.high = high
        self.low = low

    def __repr__(self):
        return '<Range %r-%r >' % (self.low, self.high)
