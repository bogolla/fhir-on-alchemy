#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Range)
#  Date: 2016-03-18.


from . import element

class Range(element.Element):
    """ Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """

    __tablename__ = "Range"

    high = Column()
    """ High limit.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    low = Column()
    """ Low limit.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    def __init__(self, high, low,):
        """ Initialize all valid properties.
        """
        self.high = high
        self.low = low

    def __repr__(self):
        return '<Range %r>' % 'self.property'  # replace self.property


from . import quantity