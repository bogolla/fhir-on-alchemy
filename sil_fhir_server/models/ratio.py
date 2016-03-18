#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Ratio)
#  Date: 2016-03-18.


from . import element

class Ratio(element.Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    __tablename__ = "Ratio"

    denominator = Column()
    """ Denominator value.
        Type `Quantity` (represented as `dict` in JSON). """

    numerator = Column()
    """ Numerator value.
        Type `Quantity` (represented as `dict` in JSON). """

    def __init__(self, denominator, numerator,):
        """ Initialize all valid properties.
        """
        self.denominator = denominator
        self.numerator = numerator

    def __repr__(self):
        return '<Ratio %r>' % 'self.property'  # replace self.property


from . import quantity