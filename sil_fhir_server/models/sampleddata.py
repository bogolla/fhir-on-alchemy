#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SampledData)
#  Date: 2016-03-18.


from . import element

class SampledData(element.Element):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    __tablename__ = "SampledData"

    data = Column()
    """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """

    dimensions = Column()
    """ Number of sample points at each time point.
        Type `int`. """

    factor = Column()
    """ Multiply data by this before adding to origin.
        Type `float`. """

    lowerLimit = Column()
    """ Lower limit of detection.
        Type `float`. """

    origin = Column()
    """ Zero value and units.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    period = Column()
    """ Number of milliseconds between samples.
        Type `float`. """

    upperLimit = Column()
    """ Upper limit of detection.
        Type `float`. """

    def __init__(self, data, dimensions, factor, lowerLimit, origin, period, upperLimit,):
        """ Initialize all valid properties.
        """
        self.data = data
        self.dimensions = dimensions
        self.factor = factor
        self.lowerLimit = lowerLimit
        self.origin = origin
        self.period = period
        self.upperLimit = upperLimit

    def __repr__(self):
        return '<SampledData %r>' % 'self.property'  # replace self.property


from . import quantity