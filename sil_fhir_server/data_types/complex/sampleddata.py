#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SampledData)
#  Date: 2016-03-18.


from sqlalchemy import Column, ForeignKey
from sil_fhir_server.data_types import primitives

from . import complex_dt


class SampledData(complex_dt.ComplexElement):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    __tablename__ = "SampledData"

    data = Column(primitives.StringField)
    """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """

    dimensions = Column(primitives.IntegerField)
    """ Number of sample points at each time point.
        Type `int`. """

    factor = Column(primitives.DecimalField)
    """ Multiply data by this before adding to origin.
        Type `float`. """

    lowerLimit = Column(primitives.DecimalField)
    """ Lower limit of detection.
        Type `float`. """

    origin = Column(primitives.StringField,
                    ForeignKey('Quantity.id'))
    """ Zero value and units.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """

    period = Column(primitives.DecimalField)
    """ Number of milliseconds between samples.
        Type `float`. """

    upperLimit = Column(primitives.DecimalField)
    """ Upper limit of detection.
        Type `float`. """

    def __init__(self, data, dimensions, factor, lowerLimit, origin,
                 period, upperLimit):
        """ Initialize all valid properties. """

        self.data = data
        self.dimensions = dimensions
        self.factor = factor
        self.lowerLimit = lowerLimit
        self.origin = origin
        self.period = period
        self.upperLimit = upperLimit

    def __repr__(self):
        return '<SampledData %r>' % 'self.property'  # replace self.property
