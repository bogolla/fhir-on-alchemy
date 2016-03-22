#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Implements: FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceMetric)
#  Date: 2016-03-18.


from sqlalchemy import Column, Integer, String
from . import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """

    __tablename__ = "DeviceMetric"

    calibration = Column(DeviceMetricCalibration)
    """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """

    category = Column(primitives.StringField)
    """ measurement | setting | calculation | unspecified.
        Type `str`. """

    color = Column(primitives.StringField)
    """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """

    identifier = Column(Identifier)
    """ Unique identifier of this DeviceMetric.
        Type `Identifier` (represented as `dict` in JSON). """

    measurementPeriod = Column(Timing)
    """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """

    operationalStatus = Column(primitives.StringField)
    """ on | off | standby.
        Type `str`. """

    parent = Column(FHIRReference)
    """ Describes the link to the parent DeviceComponent.
        Type `FHIRReference` referencing `DeviceComponent` (represented as `dict` in JSON). """

    source = Column(FHIRReference)
    """ Describes the link to the source Device.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """

    type = Column(CodeableConcept)
    """ Type of metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    unit = Column(CodeableConcept)
    """ Unit of metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """

    def __init__(self, calibration, category, color, identifier, measurementPeriod, operationalStatus, parent, source, type, unit,):
        """ Initialize all valid properties.
        """
        self.calibration = calibration
        self.category = category
        self.color = color
        self.identifier = identifier
        self.measurementPeriod = measurementPeriod
        self.operationalStatus = operationalStatus
        self.parent = parent
        self.source = source
        self.type = type
        self.unit = unit

    def __repr__(self):
        return '<DeviceMetric %r>' % 'self.property'  # replace self.property


from sqlalchemy import Column, Integer, String
from . import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """

    __tablename__ = "DeviceMetricCalibration"

    state = Column(primitives.StringField)
    """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """

    time = Column(FHIRDate)
    """ Describes the time last calibration has been performed.
        Type `FHIRDate` (represented as `str` in JSON). """

    type = Column(primitives.StringField)
    """ unspecified | offset | gain | two-point.
        Type `str`. """

    def __init__(self, state, time, type,):
        """ Initialize all valid properties.
        """
        self.state = state
        self.time = time
        self.type = type

    def __repr__(self):
        return '<DeviceMetricCalibration %r>' % 'self.property'  # replace self.property


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing